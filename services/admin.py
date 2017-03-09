# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from feincms.admin import tree_editor
from tinymce.widgets import TinyMCE
#незабываем импорт
from services.models import Service
from simpleseo.admin import seo_inline
from django.contrib.admin.actions import delete_selected as delete_selected_item

from simplesitemap.admin import map_inline


class ServiceForm(forms.ModelForm):
    url = forms.RegexField(label='slug', max_length=100, regex=r'^[-\w\_]+$',
        error_message = u"Значение должно состоять только из букв, цифр "
                        u"и символов подчеркивания, тире.")
    content = forms.CharField(widget=TinyMCE, label=u'Содержимое', required=False)

    class Meta:
        model = Service


class ServiceAdmin(tree_editor.TreeEditor):
    form = ServiceForm
    list_display = ('url','menu_title', 'is_visible')
    list_editable = ('menu_title','is_visible',)
    search_fields = ('url', 'title')
    prepopulated_fields = {"url": ("title",)}
    #Тут втыкаем новое сео
    inlines = [seo_inline(),map_inline(),]


    def render_change_form(self, request, context, *args, **kwargs):
         if 'obj' in kwargs:
            context['adminform'].form.fields['parent'].queryset = Service.objects.all().exclude(pk=kwargs['obj'].pk)
         return super(ServiceAdmin, self).render_change_form(request, context, args, kwargs)

    def get_actions(self, request):
        actions = super(ServiceAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            actions['delete_selected'] = (delete_selected_item, 'delete_selected', u"Удалить выбранные страницы сайта")
        return actions
        
admin.site.register(Service, ServiceAdmin)