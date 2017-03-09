# -*- coding: utf-8 -*-

from django import template

from main.utils import _get_gmaps_url

register = template.Library()


@register.simple_tag
def get_gmaps_url():
    return _get_gmaps_url()