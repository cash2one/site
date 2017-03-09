# -*- coding: utf-8 -*-
import re

from ipware.ip import get_ip
from django.core.validators import ip_address_validators
from django.core.exceptions import ValidationError
from flatpages.models import FlatPage
from constance import config


def get_flatpage_by_type_or_none(pagetype):
    if pagetype:
        flatpages = FlatPage.objects.filter(type=pagetype)
        if flatpages:
            return flatpages[0]
    else:
        return None


def validate_NO_href(value):
    if type(value) == unicode:
        if re.findall("(http:|https:)", value):
            raise ValidationError(u'%s содержит ссылку' % value)


def get_ip_or_none(request):
    try:
        ip = get_ip(request)
        ip_address_validators('both', ip)
    except ValidationError:
        ip = None
    return ip


def _get_gmaps_url():
    if config.GMAPS_KEY:
        google_api_link = 'http://maps.googleapis.com/maps/api/js?v=3.exp&key=' + config.GMAPS_KEY
    else:
        google_api_link = 'http://maps.googleapis.com/maps/api/js?v=3.exp'

    return google_api_link
