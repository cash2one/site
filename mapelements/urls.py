# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('mapelements.views',
    url(r'^render-map/', 'render_map', name='render-map'),
    url(r'^render-marker-data/', 'render_marker_data', name='render-marker-data')
)