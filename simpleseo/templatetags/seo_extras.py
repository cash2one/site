# -*- coding: utf-8 -*-
from constance import config
from django import template
from django.contrib.contenttypes.models import ContentType
from flatpages.models import IndexPage
from main.models import DefaultSettings
from simpleseo.models import BasicMetadata

register = template.Library()


@register.inclusion_tag('simpleseo/templatetags/seo_head.html', takes_context=False)
def get_seo(element):
    try:
        site = DefaultSettings.objects.all()[0]
    except:
        for site in DefaultSettings.objects.all():
            site.delete()
        site = DefaultSettings.objects.create(site_id=1)

    metadata = {'title': site.title, 'keywords': site.keysword, 'description': site.descriptions, }
    try:
        ### хак для главной страницы, так как рендерится она класом "посмотреть шаблон" и не передается объект главной
        if 'index' == element:
            element = IndexPage.objects.all()[0]
            ### конец хака
        metadata = BasicMetadata.objects.filter(page=element)
        if metadata.count() > 0:
            metadata = metadata[0]
            if len(metadata.title) == 0:
                metadata.title = element.get_title()
        else:
            metadata.title = element.get_title()
    except Exception, e:
        print e
    return {'metadata': metadata}