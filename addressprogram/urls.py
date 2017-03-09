# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('addressprogram.views',
    url(r'^city/(?P<slug>([-\w]+))/$', 'get_city_detail', name='city_detail'),
    url(r'^construction_list/$', 'construction_list', name='construction-list'),
    url(r'^construction/(?P<slug>([-\w]+))/$', 'construction_detail', name='construction-detail'),
    url(r'^program/$', 'get_program_list', name='program_list'),
    url(r'^program/(?P<passport_id>\d+)/$', 'get_passport_detail', name='passport_detail'),
    url(r'^program_print/(?P<passport_id>\d+)/$', 'get_passport_print', name='passport-print-preview'),
    url(r'^passport_(?P<passport_id>\d+)\.pdf$', 'get_passport_pdf', name='get-passport-pdf'),
    url(r'^get_geobject_info/$', 'get_geobject_info', name='get-geobject-info')
)
