# coding=utf-8
import json

from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.template.loader import render_to_string
from easy_pdf.rendering import render_to_pdf_response

from addressprogram.forms import AdvertisingFilterSpaceForm, LetterChoices
from addressprogram.models import City, AdvertisingSpace, Construction
from constance.models import Config
from main.utils import get_flatpage_by_type_or_none
from main.views import simple_pagination
from order.card import ShoppingCart


def get_city_detail(request, slug):
    cities = City.objects.all().filter(is_visible=True)
    item = get_object_or_404(cities, slug=slug)
    item_set = cities.exclude(slug=item.slug)
    constructions = Construction.objects.filter(show_in_city=True)
    geoobjects = AdvertisingSpace.objects.filter(
        address__city=item, address__prod__show_in_city=True).order_by('address')
    breadcrumbs = [
        {"title": item.name}
    ]
    context = {
        'cities': cities,
        'item': item,
        'item_set': item_set,
        'constructions': constructions,
        'geoobjects': geoobjects,
        'breadcrumbs': breadcrumbs
    }
    return render(request, "addressprogram/city_detail.html", context)


def construction_list(request):
    flatpage = get_flatpage_by_type_or_none("requirements")
    context = {
        'products': Construction.objects.filter(show=True, show_in_main=True),
        'page_url': reverse("program:construction-list"),
        'flatpage': flatpage,
        'breadcrumbs': [
            {"title": flatpage.title if flatpage else u"Продукты"},
        ]
    }
    return render(request, "addressprogram/construction_list.html", context)


def construction_detail(request, slug):
    construction = get_object_or_404(Construction, slug=slug)
    flatpage = get_flatpage_by_type_or_none("requirements")
    context = {
        'construction': construction,
        'page_url': reverse("program:program_list"),
        'breadcrumbs': [
            {"title": flatpage.title if flatpage else u"Продукты", "url": reverse("program:construction-list")},
            {"title": construction.name}
        ]
    }
    return render(request, "addressprogram/construction_detail.html", context)


def get_program_list(request):
    passports = AdvertisingSpace.objects.filter(is_visible=True).exclude(address__address=None)

    per_page = Config.get_by_key('PROGRAM_PER_PAGE')

    current_letter = None
    letters = LetterChoices.get_letters()

    request_data = None
    advertising_form = AdvertisingFilterSpaceForm()

    if request.GET:
        request_data = request.GET
        advertising_form = AdvertisingFilterSpaceForm(request_data)
        if advertising_form.is_valid():
            if advertising_form.cleaned_data.get("city"):
                passports = passports.filter(address__city=advertising_form.cleaned_data.get("city"))
            if advertising_form.cleaned_data.get("adv_type"):
                passports = passports.filter(type=advertising_form.cleaned_data.get("adv_type"))
            if advertising_form.cleaned_data.get("search"):
                query = advertising_form.cleaned_data.get("search")
                passports = passports.filter(Q(address__address__icontains=query) | Q(gid__icontains=query))
            if advertising_form.cleaned_data.get("letters"):
                current_letter = LetterChoices.resolve_by_value(advertising_form.cleaned_data.get("letters"))
                if current_letter:
                    passports = passports.filter(address__address__istartswith=current_letter)
            if advertising_form.cleaned_data.get("per_page"):
                per_page = advertising_form.cleaned_data.get("per_page")
            if advertising_form.cleaned_data.get("per_page") == 'True':
                per_page = passports.count()
                if per_page == 0:
                    per_page = 1

    items = simple_pagination(request, passports, per_page)
    item_list = items.object_list

    # TODO: это всё работает, он очюнеэффективно, нужно bulk_add, bulk_delete какие-нибудь
    cart = ShoppingCart(request)
    cart_items = cart.get_items()

    if item_list:
        selected_passports = []
        if request_data:
            if request_data.get("make_order"):
                form_selected_passports = map(long, request_data.getlist("cpid"))
                for item in item_list:
                    if item.id in form_selected_passports:
                        item.in_cart = True
                        cart.smart_add(item)
                    else:
                        cart.smart_remove(item)

                        # TODO: свернуть else в одну
            else:
                cart_items = cart.get_items()
                for c in cart_items:
                    selected_passports.append(c.get_item().id)
                for item in item_list:
                    if item.id in selected_passports:
                        item.in_cart = True
        else:
            cart_items = cart.get_items()
            for c in cart_items:
                selected_passports.append(c.get_item().id)
            for item in item_list:
                if item.id in selected_passports:
                    item.in_cart = True

    cart_item_counter = cart_items.count()
    temp_items = []
    temp_ots = []

    for item in cart.get_items():

        if item.grp == u'н/д' or item.grp == u'':
            continue
        temp_items.append(item.grp.replace(',', '.'))
    cart_item_grp = sum(map(float, temp_items))
    for item in cart.get_items():
        if item.ots == u'н/д' or item.ots == u'':
            continue
        temp_ots.append(item.ots.replace(',', '.'))
    cart_item_ots = sum(map(float, temp_ots))

    context = {
        'advertising_form': advertising_form,
        'current_letter': current_letter,
        'letters': letters,
        'cart_item_counter': cart_item_counter,
        'cart_item_grp': cart_item_grp,
        'cart_item_ots': cart_item_ots,
        'item_list': item_list,
        'items': items,
        'per_page': per_page,
        'flatpage': get_flatpage_by_type_or_none("program"),
        'page_url': reverse("program:program_list"),
        'breadcrumbs': [{"title": "Адресная программа"}]
    }

    if request.is_ajax():
        return HttpResponse(json.dumps({
            'data': render_to_string('addressprogram/templatetags/ajax_program_list_inner.html', context)
        }), mimetype="application/json")

    return render(request, "addressprogram/program_list.html", context)


def get_geobject_info(request):
    if request.GET and request.is_ajax():
        data = {"success": False}
        markers = AdvertisingSpace.objects.filter(id=request.GET.get("id", None))
        if markers:
            html = render_to_string("addressprogram/templatetags/marker_data.html", {"marker": markers[0]})
            data.update({"success": True, "html_content": html})

        return HttpResponse(json.dumps(data), mimetype="application/json")
    else:
        return HttpResponseRedirect("/")


def get_passport_detail(request, passport_id):
    cart = ShoppingCart(request)
    cart_items = cart.get_items()
    try:
        passport = get_object_or_404(AdvertisingSpace, pk=passport_id)
    except:
        raise Http404
    try:
        other = AdvertisingSpace.objects.filter(address=passport.address_id)
    except:
        raise Http404
    page_url = reverse("program:program_list")
    breadcrumbs = [
        {"title": "Адресная программа", "url": page_url},
        {"title": passport.address.address}
    ]
    images = []  # Собираем изображения текущего паспорта объекта
    if passport.get_primary_image():
        images.append(passport.get_primary_image())
    if passport.get_secondary_images():
        images += list(passport.get_secondary_images())

    if request.POST:
        passport = AdvertisingSpace.objects.get(id=passport_id)
        cart = ShoppingCart(request)
        for item in cart:
            if item.product == passport:
                cart.update(item.id, item.quantity)
        item = cart.smart_add(passport)

    cart_item_counter = cart_items.count()  # Счётчик паспортов добавленных в карзину
    temp_item = []
    temp_ots = []
    for item in cart.get_items():
        if item.grp == u'н/д':
            continue
        temp_item.append(item.grp.replace(',', '.'))
    cart_item_grp = sum(map(float, temp_item))
    for item in cart.get_items():
        if item.ots == u'н/д':
            continue
        temp_ots.append(item.ots.replace(',', '.'))
    cart_item_ots = sum(map(float, temp_ots))
    return render(request, "addressprogram/passport_detail.html", locals())


def get_passport_pdf(request, passport_id):
    passport = get_object_or_404(AdvertisingSpace, id=passport_id)
    if passport.has_print:
        context = {
            'title': passport.address,
            'img': passport.get_print_image_url()
        }

        return render_to_pdf_response(
            request,
            'addressprogram/print.html',
            context
        )
    return redirect('/')


def get_passport_print(request, passport_id):
    cart = ShoppingCart(request)
    cart_items = cart.get_items()
    try:
        passport = get_object_or_404(AdvertisingSpace, pk=passport_id)
    except:
        raise Http404
    try:
        other = AdvertisingSpace.objects.filter(address=passport.address_id).order_by('side')
    except:
        raise Http404
    page_url = reverse("program:program_list")
    breadcrumbs = [
        {"title": "Адресная программа", "url": page_url},
        {"title": passport.address.address}
    ]
    images = []
    if passport.get_primary_image():
        images.append(passport.get_primary_image())
    if passport.get_secondary_images():
        images += list(passport.get_secondary_images())

    if request.POST:
        passport = AdvertisingSpace.objects.get(id=passport_id)
        cart = ShoppingCart(request)
        for item in cart:
            if item.product == passport:
                cart.update(item.id, item.quantity)
        item = cart.smart_add(passport)

    cart_item_counter = cart_items.count()  # Счётчик паспортов добавленных в карзину
    temp_item = []
    temp_ots = []
    for item in cart.get_items():
        if item.grp == u'н/д':
            continue
        temp_item.append(item.grp.replace(',', '.'))
    cart_item_grp = sum(map(float, temp_item))
    for item in cart.get_items():
        if item.ots == u'н/д':
            continue
        temp_ots.append(item.ots.replace(',', '.'))
    cart_item_ots = sum(map(float, temp_ots))

    return render(request, "addressprogram/passport_detail_print.html", locals())
