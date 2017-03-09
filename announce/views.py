# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from constance.models import Config
from main.utils import get_flatpage_by_type_or_none
from models import Announce
from main.views import simple_pagination


def announce_list(request=None):
    per_page = Config.get_by_key('ANNOUNCES_PER_PAGE')
    flatpage = get_flatpage_by_type_or_none("announce")
    page_url = reverse("announce:announce-list")
    breadcrumbs = [{"title": "Анонсы"}]
    items = simple_pagination(request, Announce.objects.filter(is_visible=True).order_by("-created_at"), per_page)
    items_list = items.object_list
    return render(request, "announce/list.html", locals())


def announce_detail(request, slug):
    item = get_object_or_404(Announce, slug=slug)
    page_url = reverse("announce:announce-list")
    breadcrumbs = [
        {"title": "Анонсы", "url": page_url},
        {"title": item.title}
    ]

    return render(request, "announce/detail.html", locals())