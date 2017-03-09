# -*- coding: utf-8 -*-
from django import forms
from tinymce.widgets import TinyMCE

from constance.models import Config
from main.settings import CONSTANCE_CONFIG


class ConfigTempForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ConfigTempForm, self).__init__(*args, **kwargs)
        for k, field in self.fields.items():
            if 'required' in field.error_messages:
                field.error_messages['required'] = u'Это поле обязательно!'
            if 'invalid' in field.error_messages:
                field.error_messages['invalid'] = u'Это поле заполнено неверно!'


def preformfield(type_field, label, init_value, helptext, required=False):
    if type_field == 'bool':
        return forms.BooleanField(
            label=label,
            help_text=helptext,
            initial=init_value,
            required=required)
    elif type_field == 'int':
        return forms.IntegerField(
            label=label,
            help_text=helptext,
            initial=init_value,
            required=required)
    elif type_field == 'float':
        return forms.FloatField(
            label=label,
            help_text=helptext,
            initial=init_value,
            required=required)
    elif type_field == 'char':
        return forms.CharField(
            label=label,
            help_text=helptext,
            initial=init_value,
            required=required)
    elif type_field == 'email':
        return forms.EmailField(
            label=label,
            help_text=helptext,
            initial=init_value,
            required=required,
            widget=forms.TextInput(attrs={"class": "vTextField"})
        )

    elif type_field == 'emails':
        return forms.EmailField(
            label=label,
            help_text=helptext,
            initial=init_value,
            required=required,
            widget=forms.Textarea()
        )

    elif type_field == 'text':
        return forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 80}),
                               label=label,
                               help_text=helptext,
                               initial=init_value,
                               required=required)

    elif type_field == 'wysiwyg':
        return forms.CharField(widget=TinyMCE(attrs={'rows': 3, 'cols': 40},
                                              mce_attrs={'width': '500px', 'height': '100px', 'theme': 'simple'}),
                               label=label,
                               help_text=helptext,
                               initial=init_value,
                               required=required)

    return forms.CharField(widget=forms.CharField,
                           label=label,
                           help_text=helptext,
                           initial='no valid',
                           required=False)


class ConfigForm(ConfigTempForm):
    def __init__(self, *args, **kwargs):
        for field in CONSTANCE_CONFIG:
            dbobj, created = Config.objects.get_or_create(key=field[0])
            if created:
                dbobj.value = field[1][0]
                dbobj.save()

            # TODO: сахар!
            count_field = len(field)
            if count_field == 3:
                self.base_fields[field[0]] = preformfield(type_field=field[2],
                                                          label=field[1][1],
                                                          init_value=dbobj.value,
                                                          helptext='',
                                                          required=False,

                                                          )

            elif count_field == 4:
                self.base_fields[field[0]] = preformfield(type_field=field[2],
                                                          label=field[1][1],
                                                          init_value=dbobj.value,
                                                          helptext='',
                                                          required=field[3],
                                                          )
            elif count_field == 5:
                self.base_fields[field[0]] = preformfield(type_field=field[2],
                                                          label=field[1][1],
                                                          init_value=dbobj.value,
                                                          helptext=field[4],
                                                          required=field[3],
                                                          )

            else:
                self.base_fields[field[0]] = preformfield(type_field='char',
                                                          label=field[1][1],
                                                          init_value=dbobj.value,
                                                          helptext='',
                                                          required=False,
                                                          )

        forms.Form.__init__(self, *args, **kwargs)
