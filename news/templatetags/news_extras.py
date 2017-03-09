# -*- coding: utf-8 -*-

from django import template
from news.models import News
from flatpages.models import IndexPage

register = template.Library()


@register.inclusion_tag('news/templatetags/index_news.html')
def index_news():
    return {'last_news': News.objects.filter(is_visible=True, is_visible_main=True).order_by("-created_at")}
