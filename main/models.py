# -*- coding: utf-8 -*-
from django.contrib.sites.models import Site
from django.db import models

from .fields import AutoOneToOneField


class RobotsSettings(models.Model):
    site = AutoOneToOneField(Site, related_name='robots_settings')
    robots = models.TextField(default='User-Agent: *\nDisallow: /admin', verbose_name=u'robots.txt',blank=True,null=True,)

    def __unicode__(self):
        return u''

    class Meta:
        verbose_name = u'настройки robots.txt'
        verbose_name_plural = u'настройки robots.txt'


class YaSettings(models.Model):
    site = AutoOneToOneField(Site, related_name='metrica_settings')
    metrica = models.TextField(default='<script></script>', verbose_name=u'код метрики',blank=True,null=True,)

    def __unicode__(self):
        return u''

    class Meta:
        verbose_name = u'настройки яндекс метрики'
        verbose_name_plural = u'настройки яндекс метрики'


class MetaSettings(models.Model):
    site = AutoOneToOneField(Site, related_name='meta_settings')
    meta = models.TextField(default='', verbose_name=u'код мета',blank=True,null=True,)

    def __unicode__(self):
        return u''

    class Meta:
        verbose_name = u'настройки статичных метатегов'
        verbose_name_plural = u'настройки статичных метатегов'


class DefaultSettings(models.Model):
    site = AutoOneToOneField(Site, related_name='seo_settings')
    title = models.CharField(max_length=255, default='', verbose_name=u'Title по умолчанию',blank=True,null=True,)
    descriptions = models.TextField(default='', verbose_name=u'Description по умолчанию',blank=True,null=True,)
    keysword = models.TextField(default='', verbose_name=u'Keywords по умолчанию',blank=True,null=True,)

    def __unicode__(self):
        return u''

    class Meta:
        verbose_name = u'настройки метатегов по умолчанию'
        verbose_name_plural = u'настройки метатегов по умолчанию'
