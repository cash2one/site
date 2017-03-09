# -*- coding: utf-8 -*-

from django.conf.urls import *
from django.views.generic import RedirectView

urlpatterns = patterns('flatpages.views',
    url(r'^(?P<url>.*)$', 'flatpage', name='flatpage-det')
)
