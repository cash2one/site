# -*- coding: utf-8 -*-
from django.contrib import messages
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from flatpages.models import Manager
from forms import FeedbakForm, FeedbackManagerForm
from main.utils import get_ip_or_none
from message.models import Mail, Message
from models import Feedback
from constance import config
from django.core.mail import EmailMessage
from django.template import Template, Context
from django.contrib.sites.models import Site
import json


#TODO: дефолтный шаблон
def send_feeback_email(form, ip):
    context = {}
    if 'name' in form.cleaned_data:
        context.update({"name": form.cleaned_data['name']})
    if 'company' in form.cleaned_data:
        context.update({"company": form.cleaned_data['company']})
    if 'city' in form.cleaned_data:
        context.update({"city": form.cleaned_data['city']})
    if 'phone' in form.cleaned_data:
        context.update({"phone": form.cleaned_data['phone']})
    if 'email' in form.cleaned_data:
        context.update({"email": form.cleaned_data['email']})
    if 'message' in form.cleaned_data:
        context.update({"message": form.cleaned_data['message']})

    mail_to = config.MANAGER_EMAIL.replace(' ', '').split(',')
    email_from = config.EMAIL_FROM.replace(' ', '').split(',')[0]
    domain = Site.objects.get_current().domain
    context.update({"SITE": domain})

    mail_to_client = [context.get("email")]
    mail_subject = Mail.objects.filter(type="contacts_email")[0].subject
    mail_template = Mail.objects.filter(type="contacts_email")[0].mail
    mail_message = Template(mail_template).render(Context(context))
    mail = EmailMessage(mail_subject, mail_message, email_from, mail_to)
    mail.content_subtype = 'html'
    mail.send()

    mail_client = EmailMessage(mail_subject, mail_message, email_from, mail_to_client)
    mail_client.content_subtype = 'html'
    mail_client.send()

    feedback = Feedback()
    feedback.ip = ip
    feedback.name = context.get("name", "")
    feedback.company = context.get("company", "")
    feedback.city = context.get("city", "")
    feedback.phone = context.get("phone", "")
    feedback.email = context.get("email", "")
    feedback.message = context.get("message", "")
    feedback.save()


def process_feedback_form(request):
    breadcrumbs = [{"title": "Обратная связь"}]

    if request.method == 'POST':
        ip = get_ip_or_none(request)
        form = FeedbakForm(request.POST)
        if form.is_valid() and ip:
            send_feeback_email(form, ip)
            try:
                mess = Message.objects.filter(type='message_after_feedback_form')[0].message
            except:
                mess = "<p>Cпасибо</p>"
            messages.success(request, mess)

            respond = {"success": True, "form_errors": ''}
        else:
            respond = {"success": False, "form_errors": form.errors}

        if request.is_ajax():
            return HttpResponse(json.dumps(respond), mimetype="application/json")

    else:
        form = FeedbakForm()

    return render(request, 'feedback/form_page.html', {'feedback_form': form, "breadcrumbs": breadcrumbs})


def send_feeback_to_manager(form, ip):
    context = {}
    if 'name' in form.cleaned_data:
        context.update({"name": form.cleaned_data['name']})
    if 'company' in form.cleaned_data:
        context.update({"company": form.cleaned_data['company']})
    if 'city' in form.cleaned_data:
        context.update({"city": form.cleaned_data['city']})
    if 'phone' in form.cleaned_data:
        context.update({"phone": form.cleaned_data['phone']})
    if 'email' in form.cleaned_data:
        context.update({"email": form.cleaned_data['email']})
    if 'message' in form.cleaned_data:
        context.update({"message": form.cleaned_data['message']})
    if 'manager' in form.cleaned_data:
        context.update({"manager": form.cleaned_data['manager']})
    try:
        manager = get_object_or_404(Manager, pk=context.get("manager", ""))
    except:
        raise Http404
    mail_to = [manager.email]
    mail_to_other = [manager.sub_email]
    email_from = config.EMAIL_FROM.replace(' ', '').split(',')[0]
    domain = Site.objects.get_current().domain
    context.update({"SITE": domain})

    mail_to_client = [context.get("email")]
    mail_subject = Mail.objects.filter(type="manager_email")[0].subject
    mail_template = Mail.objects.filter(type="manager_email")[0].mail
    mail_message = Template(mail_template).render(Context(context))
    mail = EmailMessage(mail_subject, mail_message, email_from, mail_to)
    mail.content_subtype = 'html'
    mail.send()

    mail_other = EmailMessage(mail_subject, mail_message, email_from, mail_to_other)
    mail_other.content_subtype = 'html'
    mail_other.send()

    mail_client = EmailMessage(mail_subject, mail_message, email_from, mail_to_client)
    mail_client.content_subtype = 'html'
    mail_client.send()

    feedback = Feedback()
    feedback.ip = ip
    feedback.name = context.get("name", "")
    feedback.company = context.get("company", "")
    feedback.city = context.get("city", "")
    feedback.phone = context.get("phone", "")
    feedback.email = context.get("email", "")
    feedback.message = context.get("message", "")
    feedback.save()


def process_feedback_manager(request):
    breadcrumbs = [{"title": "Обратная связь"}]

    if request.method == 'POST':
        ip = get_ip_or_none(request)
        form = FeedbackManagerForm(request.POST)
        if form.is_valid() and ip:
            send_feeback_to_manager(form, ip)

            try:
                mess = Message.objects.filter(type='message_after_feedback_form')[0].message
            except:
                mess = "<p>Cпасибо</p>"
            messages.success(request, mess)

            respond = {"success": True, "form_errors": ''}
        else:
            respond = {"success": False, "form_errors": form.errors}

        if request.is_ajax():
            return HttpResponse(json.dumps(respond), mimetype="application/json")

    else:
        form = FeedbakForm()

    return render(request, 'feedback/form_page.html', {'feedback_form': form, "breadcrumbs": breadcrumbs})
