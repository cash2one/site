# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('news.views',
                       url(r'^novosti/$', 'news_list', name='news-list'),
                       url(r'^novosti/(?P<slug>([-\w]+))/$', 'news_detail', name='news-detail'),
                       )
