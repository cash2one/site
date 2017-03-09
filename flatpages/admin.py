# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy
from feincms.admin import tree_editor
from tinymce.widgets import TinyMCE
from flatpages.models import FlatPage, IndexPage, Advantage, Manager, IndexAbout
from main import settings
# незабываем импорт
from simpleseo.admin import seo_inline
from django.contrib.admin.actions import delete_selected as delete_selected_item

from simplesitemap.admin import map_inline


class FlatpageForm(forms.ModelForm):
    url = forms.RegexField(label='URL', max_length=100, regex=r'^[-\w/\.~]+$',
                           error_message=u"Значение должно состоять только из букв, цифр "
                                         u"и символов точки, подчеркивания, тире, косой черты и тильды.")
    content = forms.CharField(widget=TinyMCE, label=u'Содержимое', required=False)

    class Meta:
        model = FlatPage


class FlatPageAdmin(tree_editor.TreeEditor):
    form = FlatpageForm
    list_display = ('url', 'type', 'show_in_menu', 'show_in_side_menu', 'is_visible', 'order',)
    list_editable = ('show_in_menu', 'is_visible', 'show_in_side_menu', 'order',)
    search_fields = ('url', 'title')
    prepopulated_fields = {"url": ("title",)}
    # Тут втыкаем новое сео
    inlines = [seo_inline(), map_inline(), ]

    def render_change_form(self, request, context, *args, **kwargs):
        if 'obj' in kwargs:
            context['adminform'].form.fields['parent'].queryset = FlatPage.objects.all().exclude(pk=kwargs['obj'].pk)
        return super(FlatPageAdmin, self).render_change_form(request, context, args, kwargs)

    def get_actions(self, request):
        actions = super(FlatPageAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            actions['delete_selected'] = (delete_selected_item, 'delete_selected', u"Удалить выбранные страницы сайта")
        return actions


admin.site.register(FlatPage, FlatPageAdmin)


class IndexPageAdmin(admin.ModelAdmin):
    # Тут втыкаем новое сео
    inlines = [seo_inline()]

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

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content',):
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 10},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ), help_text=u'Содержимое страницы', label=u'Содержимое страницы', required=False)

        if db_field.name in ('seo_text',):
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 10},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ), help_text=u'Текст внизу на главной', label=u'Сео Текст', required=False)

        return super(IndexPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(IndexPage, IndexPageAdmin)


class IndexAboutAdmin(admin.ModelAdmin):
    inlines = [seo_inline()]

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

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('left_content',):
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 10},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ), help_text=u'Содержимое левой колонки', label=u'Содержимое левой колонки', required=False)

        if db_field.name in ('right_content',):
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 10},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ), help_text=u'Содержимое правой колонки', label=u'Содержимое правой колонки', required=False)

        if db_field.name in ('seo_text',):
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 10},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ), help_text=u'Текст внизу на главной', label=u'Сео Текст', required=False)

        return super(IndexAboutAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(IndexAbout, IndexAboutAdmin)


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'show',)
    list_editable = ('order', 'show')


admin.site.register(Advantage, AdvantageAdmin)


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'order', 'show',)
    list_editable = ('order', 'show',)
    list_display_links = ('full_name',)


admin.site.register(Manager, ManagerAdmin)
