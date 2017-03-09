# -*- coding: utf-8 -*-

from django import template
from slider.models import Slide

register = template.Library()


@register.inclusion_tag('slider/templatetags/slider.html')
def slider():
    return {'slides': list(Slide.objects.filter(show=True))}
