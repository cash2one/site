# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.shortcuts import render_to_response
from django.template import RequestContext

from simplesitemap.models import BasicSitemapData


def sitemap_gen(request):
    host = Site.objects.get_current().domain
    if not host.startswith('http://'):
        host = 'http://%s'%host
    items = BasicSitemapData.objects.filter(item_disable=False).order_by('-order_num')

    return render_to_response('simplesitemap/sitemap.html', locals(), context_instance=RequestContext(request),
                              mimetype="application/xhtml+xml")