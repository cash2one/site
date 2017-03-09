# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ValidationError
import re

from django.forms import ChoiceField, HiddenInput

from main.utils import validate_NO_href


class CustomForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CustomForm, self).__init__(*args, **kwargs)
        for k, field in self.fields.items():
            field.validators.append(validate_NO_href)
            if 'required' in field.error_messages:
                field.error_messages['required'] = u'Это поле обязательно!'
            if 'invalid' in field.error_messages:
                field.error_messages['invalid'] = u'Это поле заполнено неверно!'

def validate_phone(value):
    if not re.match("^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{6,10}", value):
        raise ValidationError(u'%s не является правильным номером' % value)


def validate_email(value):
    if not re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", value):
        raise ValidationError(u'%s не является корректным email' % value)


class FeedbakForm(CustomForm):
    name = forms.CharField(
        max_length=255,
        label=u"Ф.И.О.",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "xcols": 6
        })
    )

    company = forms.CharField(
        max_length=255,
        label=u"Компания",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "xcols": 6
        })
    )

    city = forms.CharField(
        max_length=255,
        label=u"Ваш город",
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "xcols": 6
        })
    )

    phone = forms.CharField(
        label=u"Телефон",
        validators=[validate_phone],
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "type": "phone",
            "xcols": 6
        })
    )

    email = forms.EmailField(
        label=u"E-mail",
        validators=[validate_email],
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "type": "email",
            "xcols": 6
        })
    )

    message = forms.CharField(
        label=u"Сообщение",
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "xcols": 12,
            "rows": 4
        })
    )


class FeedbackManagerForm(FeedbakForm):
    manager = forms.CharField(
        label=u'manager',
        required=True,
        widget=HiddenInput(),
    )
