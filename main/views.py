# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from flatpages.models import FlatPage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def change_theme(request):
    if request.GET.has_key("theme"):
        theme = request.GET.get("theme")
        request.session.update({ "theme":theme })
    url = "/"
    try:
        url = request.META.get("HTTP_REFERER")
    except:
        pass
    return HttpResponseRedirect(url)


def simple_pagination(request, items, per_page=4):
    paginator = Paginator(items, per_page)

    try:
        page = int(request.GET['page'])
    except:
        page = 1

    try:
        items_list = paginator.page(page)
    except PageNotAnInteger:
        items_list = paginator.page(1)
    except EmptyPage:
        items_list = paginator.page(paginator.num_pages)

    #to display a range of 6 page
    if items_list.number < 4:
        if paginator.num_pages >= 5:
            items_list.range_page = paginator.page_range[0:5]
        else:
            items_list.range_page = paginator.page_range[0:paginator.num_pages]
    elif (items_list.number + 2) > paginator.num_pages:
        items_list.range_page = paginator.page_range[paginator.num_pages - 5:paginator.num_pages]
    else:
        items_list.range_page = paginator.page_range[items_list.number - 3:items_list.number + 2]

    return items_list


def close_special_modal(request):
    if request.session:
        request.session["snc_dismissed"] = True
    url = "/"
    try:
        url = request.META.get("HTTP_REFERER")
    except:
        pass

    return HttpResponseRedirect(url)