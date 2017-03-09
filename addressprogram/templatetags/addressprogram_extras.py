# -*- coding: utf-8 -*-

from django import template

from addressprogram.models import City, Construction, GeoObject
from main.utils import get_flatpage_by_type_or_none

register = template.Library()


@register.inclusion_tag('templatetags/footer/footer_cities.html')
def get_index_cities():
    sets = City.objects.filter(is_visible=True)
    if sets.count() <= 7:
        cities = sets.order_by('order')
        return {'cities': cities}
    else:
        cities = sets.order_by('order')[:7]
        return {'cities': cities}


@register.inclusion_tag('addressprogram/templatetags/index_city_map.html')
def index_city_map():
    cities = City.objects.filter(is_visible=True)

    return {'cities': cities}


@register.inclusion_tag('addressprogram/templatetags/index_product.html')
def get_index_product():
    products = Construction.objects.filter(show=True, show_in_main=True)
    if products:
        return {'products': products}


@register.inclusion_tag('addressprogram/templatetags/footer_constructions.html')
def get_footer_constructions():
    constructions = Construction.objects.filter(show=True, show_footer=True)
    flatpage = get_flatpage_by_type_or_none("requirements")
    return {
        'constructions': constructions,
        'flatpage': flatpage,
    }