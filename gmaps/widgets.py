# -*- coding: utf-8 -*-

import re

from django.forms import widgets
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.core.exceptions import ValidationError
from main.utils import _get_gmaps_url


def offrange(value,range_):
    return bool(-range_ >= value or value >= range_)


def validate_coordinates(value):
    if not re.match("^-?\d{1,2}\.?\d+,\s*-?\d{1,3}\.(?=\d)\d*\s*", value):
        raise ValidationError(u'%s не является валидным значением для координат1' % value)
    else:
        lat, lon = map(float,value.replace(" ", "").split(','))
        if offrange(lat, 90) or offrange(lon, 180):
            raise ValidationError(u'%s не является валидным значением для координат2' % value)


class jsser(object):
    def __iter__(self):
        return (i for i in (
            '/static/grappelli/jquery/jquery-1.7.2.min.js',
            _get_gmaps_url()+'&libraries=places',
            '/media/js/modules/google-maps-admin.js')
        )


class GoogleMapsCoordinatesWidget(widgets.TextInput):
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            final_attrs['value'] = force_unicode(self._format_value(value))
        return mark_safe(
            u'<input%s data-gma-type="coordinates" />' % flatatt(final_attrs))


class GoogleMapsAddressWidget(widgets.TextInput):
    class Media:
        css = {'all': ('/media/css/google-maps-admin.css',), }
        js = jsser()

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            final_attrs['value'] = force_unicode(self._format_value(value))
        return mark_safe(
            u'<input%s data-gma-type="address" /><div class="map_canvas_wrapper"><div id="map_canvas"></div></div>' % flatatt(final_attrs))
