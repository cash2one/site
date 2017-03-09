# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('announce.views',
    url(r'^akcii/$', 'announce_list', name='announce-list'),
    url(r'^akcii/(?P<slug>([-\w]+))/$', 'announce_detail', name='announce-detail'),
)
