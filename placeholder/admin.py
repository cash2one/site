# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from tinymce.widgets import TinyMCE
from django.core.urlresolvers import reverse
from placeholder.models import Placeholder
from main import settings

class PlaceholderAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_content')
    search_fields = ('name', 'show_content')

    fields = ("name", "template", "source_content",)

    add_form_template = "placeholder/placeholder_form.html"
    change_form_template = "placeholder/placeholder_form.html"

    def show_content(self, obj):
        return mark_safe(obj.content)

    show_content.short_description = u"Содержимое"

    def get_actions(self, request):
        actions = super(PlaceholderAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
        
    def has_add_permission(self, *args, **kwargs):
        if settings.DEBUG:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if settings.DEBUG:
            return True
        else:
            return False

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     if db_field.name in ('content',):
    #         return forms.CharField(widget=TinyMCE(
    #             attrs={'cols': 80, 'rows': 20},
    #             mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
    #         ), help_text=u'Содержание плейсхолдера', label=u'Содержимое', required=False)
    #     return super(PlaceholderAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Placeholder, PlaceholderAdmin)
