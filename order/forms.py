# -*- coding: utf-8 -*-
import re

from django.core.exceptions import ValidationError

from main.utils import validate_NO_href
from order.models import Order
from django import forms


def validate_phone(value):
    if not re.match("^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{6,10}", value):
        raise ValidationError(u'%s не является правильным номером' % value)


def validate_email(value):
    if not re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", value):
        raise ValidationError(u'%s не является корректным email' % value)

ORDER_FORM_WIDGETS = {
    "comment": forms.Textarea(
        attrs={"rows": 3}
    )
}


class OrderForm(forms.ModelForm):
    email = forms.EmailField(label=u'E-mail', required=True, validators=[validate_email])
    phone = forms.CharField(label=u'Телефон', required=True, validators=[validate_phone])
    date_start = forms.DateField(label=u'Дата начала размежиния', input_formats=["%d-%m-%Y"])
    date_end = forms.DateField(label=u'Дата окончания размещения', input_formats=["%d-%m-%Y"])

    class Meta:
        model = Order
        widgets = ORDER_FORM_WIDGETS
        exclude = ('ip',)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].validators.append(validate_NO_href)
            self.fields[field].widget.attrs['placeholder'] = self.fields[field].label
            if not self.fields[field].widget.attrs.get('class'):
                self.fields[field].widget.attrs['class'] = "form_control"
