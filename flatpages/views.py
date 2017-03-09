# -*- coding: utf-8 -*-

from flatpages.models import FlatPage, IndexPage, Manager
import json

from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect

DEFAULT_TEMPLATE = 'flatpages/default.html'
CONTACTS_TEMPLATE = 'flatpages/contacts.html'


def flatpage(request, url):
    if not url.endswith('/') and settings.APPEND_SLASH:
        return HttpResponseRedirect("%s/" % request.path)
    if not url.startswith('/'):
        url = "/" + url
    f = get_object_or_404(FlatPage, url__exact=url, is_visible=True)
    return render_flatpage(request, f)


@csrf_protect
def render_flatpage(request, f):
    context = None
    manager = []
    if f.type == "contacts":
        t = loader.get_template(CONTACTS_TEMPLATE)
        f.title = mark_safe(f.title)
        f.content = mark_safe(f.content)
        m = Manager.objects.filter(show=True).order_by('order')
        if m:
            manager = m
        c = RequestContext(request, {
            'flatpage': f,
            'breadcrumbs': f.get_breadcrumbs(),
            'context': context,
            'manager': manager
        })
        response = HttpResponse(t.render(c))
        populate_xheaders(request, response, FlatPage, f.id)
        return response
    else:
        t = loader.get_template(DEFAULT_TEMPLATE)
        f.title = mark_safe(f.title)
        f.content = mark_safe(f.content)
        c = RequestContext(request, {
            'flatpage': f,
            'breadcrumbs': f.get_breadcrumbs(),
            'context': context,
        })
        response = HttpResponse(t.render(c))
        populate_xheaders(request, response, FlatPage, f.id)
        return response
