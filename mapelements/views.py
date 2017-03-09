# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string

from main.utils import _get_gmaps_url
from mapelements.models import MapPoint


def render_marker_data(request):
    if request.POST and request.is_ajax():
        data = {"success": False}
        markers = MapPoint.objects.filter(id=request.POST.get("id", None))
        if markers:
            html = render_to_string("mapelements/marker_data.html", {"marker": markers[0]})
            data.update({"success": True, "html_content": html})

        return HttpResponse(json.dumps(data), mimetype="application/json")
    else:
        return HttpResponseRedirect("/")

def render_map(request):
    if request.POST and request.is_ajax():
        success = True
        data = {}

        markers_array = list(MapPoint.objects.filter(
            is_visible=True,
            type_of_point="default"
        ).values_list(
            "id",
            "coordinates")
        )

        if markers_array:
            markers = {
                i[0]: {"coordinates": i[1]} for i in markers_array
            }

        else:
            markers = []

        data.update({
            "success": success,
            "has_markers": True if markers_array else False,
            "markers": markers,
            "api_script_url": _get_gmaps_url(),
        })

        return HttpResponse(json.dumps(data), mimetype="application/json")
    else:
        return HttpResponseRedirect("/")