# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms

from gmaps.widgets import GoogleMapsAddressWidget, GoogleMapsCoordinatesWidget, validate_coordinates
from models import MapPoint


class MapPointAdminForm(forms.ModelForm):
    coordinates = forms.CharField(
        widget=GoogleMapsCoordinatesWidget(),
        validators=[validate_coordinates]
    )

    class Meta:
        model = MapPoint
        exclude = ()
        widgets = {'address': GoogleMapsAddressWidget()}


class MapPointAdmin(admin.ModelAdmin):
    form = MapPointAdminForm

    list_display = ('name', 'is_visible', 'type_of_point',)
    list_editable = ('is_visible', )

admin.site.register(MapPoint, MapPointAdmin)