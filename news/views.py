# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

from django.shortcuts import render, get_object_or_404
from constance.models import Config
from main.utils import get_flatpage_by_type_or_none
from main.views import simple_pagination
from models import News


def news_list(request=None):
    per_page = Config.get_by_key('NEWS_PER_PAGE')
    flatpage = get_flatpage_by_type_or_none("news")
    page_url = reverse("news:news-list")

    breadcrumbs = [{"title": "Новости" }]
    items = simple_pagination(request, News.objects.filter(is_visible=True).order_by("-created_at"), per_page)
    items_list = items.object_list
    return render(request, "news/list.html", locals())


def news_detail(request, slug):
    item = get_object_or_404(News, slug=slug)

    breadcrumbs = [
        {"title": "Новости", "url": reverse("news:news-list") },
        {"title": item.title}
    ]

    footer_class = "order_floating_block"

    return render(request, "news/detail.html", locals())

