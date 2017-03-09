# -*- coding: utf-8 -*-
from django import template

from constance import config
from feedback.forms import FeedbakForm, FeedbackManagerForm

register = template.Library()


@register.inclusion_tag('feedback/forms/feedback_form.html')
def feedback_form(form=None):
    head = config.HEAD_FORM
    if not form:
        form = FeedbakForm()
    return {'form': form, 'head': head, }


@register.inclusion_tag('feedback/forms/modal_form.html')
def modal_form(form=None):
    head = config.HEAD_FORM
    if not form:
        form = FeedbakForm()
    return {'form': form, 'head': head}


@register.inclusion_tag('feedback/forms/manager_form.html')
def manager_modal_form(form=None):
    head = config.MODAL_FORM
    if not form:
        form = FeedbackManagerForm()
    return {'form': form, 'head': head}


@register.inclusion_tag('feedback/forms/contacts_form.html')
def contacts_form(form=None):
    head = config.CONTACT_FORM
    if not form:
        form = FeedbakForm()
    return {'form': form, 'head': head, }
