# coding=utf-8


import StringIO
from main.settings import PROJECT_ROOT
import os
import xlsxwriter
from django.contrib import messages
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.core.validators import email_re
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.template import Template
from django.template.loader import render_to_string
from django.utils.translation import ugettext

from addressprogram.models import Image
from constance import config
from constance.models import Config
from main.utils import get_ip_or_none
from main.views import simple_pagination
from message.models import Mail, Message
from order.card import ShoppingCart
from order.forms import OrderForm
from order.models import OrderStatus, OrderItem


def get_email_list(var):
    addresses = var.replace(' ', '').split(',')
    valid_emails = []
    for email in addresses:
        if bool(email_re.match(email)):
            valid_emails.append(email)
    return valid_emails


def send_order_email(request, template_type, default_template, order, emails_to):
    context = {
        'order': order
    }
    mail_template = get_object_or_404(Mail, type=template_type)
    try:
        subject = mail_template.subject
        host = Site.objects.get_current().domain
        if not host.startswith('http://'):
            host = 'http://%s' % host

        context.update({"domain": host})
        html_content = Template(mail_template.mail).render(Context(context))
    except:
        context.update({"error_text": 'Уведомление на почту не заполнено!'})
        subject = u'Заказы'
        html_content = render_to_string(default_template, context)

    msg = EmailMessage(subject, html_content, config.ORDER_FROM_EMAIL, emails_to)
    msg.content_subtype = "html"
    msg.send()


def get_cart(request):
    prog_url = reverse("program:program_list")
    breadcrumbs = [{"title": u"Адресная программа", "url": prog_url},
                   {"title": u"Корзина"}]
    per_page = Config.get_by_key('ORDER_PER_PAGE')
    qs = u"per_page=%s" % per_page
    cart = ShoppingCart(request)

    if request.GET:
        if request.GET.get('per_page'):
            per_page = request.GET.get('per_page')
            qs = u"per_page=%s" % per_page

        if request.GET.get('per_page') == 'show_all':
            per_page = cart.get_items().count()
            qs += u"per_page=%s" % per_page
            if per_page == 0 or per_page is None:
                per_page = 1

    items = simple_pagination(request, cart.get_items(), per_page)
    item_list = items.object_list
    return render(request, 'order/card.html', locals())


def remove_from_cart(request, item_id):
    cart = ShoppingCart(request)
    cart.remove(item_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def clear_cart(request):
    cart = ShoppingCart(request)
    cart.clear()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def checkout(request):
    # TODO: объединить в один с get_cart, убрать locals
    per_page = Config.get_by_key('ORDER_PER_PAGE')
    qs = u"per_page=%s" % per_page
    cart = ShoppingCart(request)

    if request.GET:
        if request.GET.get('per_page'):
            per_page = request.GET.get('per_page')
            qs = u"per_page=%s" % per_page

        if request.GET.get('per_page') == 'show_all':
            per_page = cart.get_items().count()
            qs += u"per_page=%s" % per_page

    items = simple_pagination(request, cart.get_items(), per_page)
    item_list = items.object_list

    breadcrumbs = [
        {"title": "Корзина", "url": reverse("order:get-cart")},
        {"title": "Оформление заказа"}
    ]

    form = OrderForm()
    if request.method == 'POST' and cart.quantity():
        ip = get_ip_or_none(request)
        form = OrderForm(request.POST)
        if form.is_valid() and ip:
            order = form.save(commit=False)
            statuses = OrderStatus.objects.filter(is_initial=True)
            if statuses:
                order.status = statuses[0]
            order.total_cost = cart.summary()
            order.ip = ip
            order.save()

            for item in cart:
                if item:
                    OrderItem.objects.create(
                        order=order,
                        passport=item.get_item(),
                        grp=item.grp,
                        ots=item.ots,
                        quantity=item.quantity
                    )

            cart.clear()
            if order.email:
                customer_emails_list = get_email_list(order.email)
                send_order_email(
                    request,
                    'customer_email',
                    'order/emails/customer_email.html',
                    order,
                    customer_emails_list
                )
            send_order_email(
                request,
                'seller_email',
                'order/emails/manager_email.html',
                order,
                get_email_list(config.ORDER_TO_EMAIL)
            )
            try:
                mess = Message.objects.filter(type='message_after_successful_order')[0].message
            except:
                mess = "<br><p>Cпасибо!</p><br>"
            messages.success(request, mess)
            return HttpResponseRedirect(reverse("order:get-cart"))
    # context = {
    #     'form': form,
    #     'cart': cart,
    #     'breadcrumbs': breadcrumbs,
    # }

    return render(request, 'order/card.html', locals())





def download_order_exel(request):
    cart = ShoppingCart(request)
    images = Image.objects.all()
    domain = Site.objects.get_current().domain
    output = StringIO.StringIO()
    if cart.quantity():
        workbook = xlsxwriter.Workbook(output)
        worksheet_o = workbook.add_worksheet(u'Заказ')
        header_format = workbook.add_format({
            'bg_color': '#68C6DB',
            'color': 'black',
            'bold': True,
            'align': 'center',
            'valign': 'top',
            'border': 1
        })
        cell_center = workbook.add_format({
            'align': 'center',
            'valign': 'top',
            'border': 1
        })
        cell_link = workbook.add_format({
            'align': 'center',
            'valign': 'top',
            'border': 1,
            'color': 'blue',
            'underline': 1
        })
        cell_left = workbook.add_format({
            'align': 'left',
            'valign': 'top',
            'border': 1
        })
        headers = [u'№', u'Тип', u'Город', u'Адрес', u'Сторона', u'Фото', u'Подсветка', u'GID', u'GRP']
        for counter, head in enumerate(headers):
            worksheet_o.write(6, counter, ugettext(head), header_format)

        # img = os.path.join(PROJECT_ROOT, 'media/uploads/addressprogram/adv_space/52AzCS.png')
        img = os.path.join(PROJECT_ROOT, 'media/upload/52azcs.png')
        worksheet_o.insert_image('C1', img, options={'x_scale': 0.35, 'y_scale': 0.35})
        for idx, item in enumerate(cart.get_items()):
            item_id = (int(item.product.id))
            image_url = get_object_or_404(images, object_id=item_id)
            first_part = 'http://'
            third_part = '/media/'
            photo_link = u''.join((first_part, domain, third_part, str(image_url.file))).encode().strip()
            row = 7 + idx
            worksheet_o.write_number(row, 0, idx + 1, cell_center)
            worksheet_o.write_string(row, 1, item.product.type.name, cell_center)
            worksheet_o.write_string(row, 2, item.product.address.city.name, cell_center)
            worksheet_o.write_string(row, 3, item.product.address.address, cell_left)
            worksheet_o.write_string(row, 4, item.product.side, cell_center)
            worksheet_o.write_url(row, 5, photo_link, cell_link, u'Фото')
            if item.product.backlight == '1' or item.product.backlight == 'yes':
                backlight = ugettext(u'Да')
            else:
                backlight = ugettext(u'Нет')
            worksheet_o.write_string(row, 6, backlight, cell_center)
            worksheet_o.write_string(row, 7, item.product.gid, cell_center)
            worksheet_o.write_string(row, 8, item.product.grp, cell_center)
        worksheet_o.set_column('A:A', 5)
        worksheet_o.set_column('B:B', 15)
        worksheet_o.set_column('C:C', 15)
        worksheet_o.set_column('D:D', 45)
        worksheet_o.set_column('E:E', 10)
        worksheet_o.set_column('F:F', 7)
        worksheet_o.set_column('G:G', 10)
        worksheet_o.set_column('H:H', 15)
        worksheet_o.set_column('I:I', 7)
        workbook.close()
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=karus.xlsx'
    response.write(output.getvalue())
    return response
