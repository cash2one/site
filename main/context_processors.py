# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.models import Site


def current_site(request):
    return {
        'site': Site.objects.get_current()
    }


def layout_debug(request):
    return {
        'LAYOUT_DEBUG': getattr(settings, 'LAYOUT_DEBUG', False)
    }
