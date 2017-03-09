# -*- coding: utf-8 -*-
from django.forms import ModelForm, Form, ModelChoiceField, CharField, Select, TextInput, ChoiceField, IntegerField, \
    HiddenInput, BooleanField

from addressprogram.models import City, Construction, AdvertisingSpace


class LetterChoices(object):
    # TODO: cache generator output
    @classmethod
    def gen(cls):
        # for l in xrange(1072, 1104):
        #     yield (unicode(l), unichr(l).upper())
        return list((unicode(i), k) for i, k in enumerate(u'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'))

    def __init__(self):
        pass

    @classmethod
    def get_letters(cls):
        return list(cls.gen())

    @classmethod
    def resolve_by_value(cls, value):
        return next((i[1] for i in cls.get_letters() if i[0] == value), None)


class AdvertisingFilterSpaceForm(Form):
    DEF_ATTRS = {"class": "form-control"}

    city = ModelChoiceField(
        queryset=City.objects.all(),
        label=u"Город",
        required=False,
        widget=Select(attrs=DEF_ATTRS)
    )

    adv_type = ModelChoiceField(
        queryset=Construction.objects.filter(show=True),
        label=u"Тип рекламного носителя",
        required=False,
        widget=Select(attrs=DEF_ATTRS)
    )

    search = CharField(
        label=u"Поиск по: адресу / GID",
        required=False,
        max_length=255,
        widget=TextInput(attrs=DEF_ATTRS)
    )

    page = IntegerField(
        required=False,
        widget=HiddenInput()
    )

    per_page = CharField(
        required=False,
        widget=HiddenInput()
    )

    letters = ChoiceField(
        choices=LetterChoices.get_letters(),
        required=False
    )
