# -*- coding: utf-8 -*-

from django import forms
from django.contrib import admin
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
from django.utils.html import format_html

from tinymce.widgets import TinyMCE

from addressprogram.models import City, Region, Image, GeoObject, Construction, AdvertisingSpace
from gmaps.widgets import GoogleMapsCoordinatesWidget, validate_coordinates, GoogleMapsAddressWidget
from simpleseo.admin import seo_inline
from simplesitemap.admin import map_inline


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')
    list_editable = ('is_visible',)
    list_display_links = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [seo_inline(), map_inline(), ]


admin.site.register(Region, RegionAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible', 'order',)
    list_editable = ('is_visible',)
    list_filter = ('is_visible',)
    list_display_links = ('name',)

    exclude = ('available_constructions',)

    prepopulated_fields = {"slug": ("name",)}

    inlines = [seo_inline(), map_inline(), ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('description',):
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 20},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ), help_text=u'Полный текст описания', label=u'Текст', required=False)
        return super(CityAdmin, self).formfield_for_dbfield(db_field, **kwargs)


admin.site.register(City, CityAdmin)


class GeoObjectAdminForm(forms.ModelForm):
    coordinates = forms.CharField(
        widget=GoogleMapsCoordinatesWidget(),
        validators=[validate_coordinates]
    )

    class Meta:
        model = GeoObject
        exclude = ('latitude','longitude')
        widgets = {'address': GoogleMapsAddressWidget()}


class GeoObjectAdmin(admin.ModelAdmin):
    form = GeoObjectAdminForm
    list_display = ('city', 'address', 'date', 'is_visible',)
    list_editable = ('is_visible',)
    list_filter = ('city', 'is_visible',)
    list_display_links = ('date', 'city', 'address',)
    search_fields = ['address', 'latitude', 'longitude']


admin.site.register(GeoObject, GeoObjectAdmin)


class ConstructionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'order', 'show', 'show_in_main', 'show_in_city', 'show_footer')
    list_display_links = ('name', 'slug',)
    list_editable = ('show', 'show_in_main', 'show_in_city', 'show_footer')

    prepopulated_fields = {"slug": ("name",)}
    fieldsets = [
        (u'Основное', {
            'classes': ('collapse',),
            'fields': ('name','date', 'slug', 'short_content', 'content',)
        }),
        (u'Отображение', {
            'classes': ('collapse',),
            'fields': ('order', 'show', 'show_in_main', 'show_in_city', 'show_footer')
        }),
        (u'Маркер', {
             'classes': ('collapse',),
             'fields':('marker_icon', 'marker_icon_active')
        }),
        (u'Пиктограммы на главной',{
             'classes': ('collapse',),
             'fields': ('icon', 'icon_hover', 'icon_active')
        })
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content',):
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 20},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ), help_text=u'Полный текст описания', label=u'Описание', required=False)
        return super(ConstructionAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Construction, ConstructionAdmin)


class ImageInline(generic.GenericStackedInline):
    model = Image
    extra = 0


class AdvertisingSpaceAdminForm(forms.ModelForm):
    class Meta:
        model = AdvertisingSpace
        exclude = ('has_print',)


class AdvertisingSpaceAdmin(admin.ModelAdmin):
    list_display = ('gid', 'address', 'side', 'grp', 'ots', 'image_status',)
    list_filter = ('gid', 'address__address', 'grp', 'ots',)
    list_display_links = ('gid', 'address',)

    inlines = [ImageInline]
    search_fields = ['address__address', 'gid']

    form = AdvertisingSpaceAdminForm

    def image_status(self, obj):
        try:
            Image.objects.filter(object_id=obj.id)
            return format_html(u"<p>Есть</p>")
        except:
            return format_html(u'<p style="background-color: red; color: yellow; text-align: center;">Пусто</p>')

    image_status.short_description = '%s' % u'Статус картинки'

admin.site.register(AdvertisingSpace, AdvertisingSpaceAdmin)
