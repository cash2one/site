# -*- coding: utf-8 -*-
from error_manag.models import ErrorMessage

from django.http import Http404
from django.conf import settings
from flatpages.views import flatpage
from django.http.response import HttpResponseNotFound
from django.template import RequestContext
from django.template.loader import render_to_string


class FlatpageFallbackMiddleware(object):
    def process_response(self, request, response):
        if response.status_code != 404:
            return response # No need to check for a flatpage for non-404 responses.
        try:
            return flatpage(request, request.path_info)
        except Http404:
            pass
        if settings.DEBUG:
            raise

        if response.status_code == 404:
            try:
                content = u'%s' % ErrorMessage.objects.get(type='404').message
            except:
                content = u'404'
            return HttpResponseNotFound(render_to_string(
                'flatpages/default_for_404.html',
                {'breadcrumbs': [{"title": "404"}],
                 'flatpage': {'content': content,}
                },
                context_instance=RequestContext(request)))
        return response
