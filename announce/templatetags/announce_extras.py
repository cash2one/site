# -*- coding: utf-8 -*-

from django import template
from announce.models import Announce
from constance import config

register = template.Library()

@register.inclusion_tag('announce/templatetags/index_announces.html')
def index_announces():
    return {'announces': Announce.objects.filter(is_visible=True, is_visible_on_main=True).order_by('-created_at')[:2]}

@register.inclusion_tag('announce/templatetags/side_menu_announce.html')
def side_menu_announce():
    return {'announces': Announce.objects.filter(is_visible=True,is_visible_inner=True).order_by('-created_at')}
