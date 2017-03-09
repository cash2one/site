# -*- coding: utf-8 -*-
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import pre_delete


class SiteXmlManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'page' in kwargs:
            kwargs['item_model'] = ContentType.objects.get_for_model(type(kwargs['page']))
            kwargs['item_id'] = kwargs['page'].pk
            del (kwargs['page'])
        return super(SiteXmlManager, self).get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        if 'page' in kwargs:
            kwargs['item_model'] = ContentType.objects.get_for_model(type(kwargs['page']))
            kwargs['item_id'] = kwargs['page'].pk
            del (kwargs['page'])
        return super(SiteXmlManager, self).filter(*args, **kwargs)


class BasicSitemapData(models.Model):
    lastmod_auto = models.DateField(verbose_name=u'Дата последней модификации автоматическая',
                                    auto_now=True,)
    lastmod_manual = models.DateField(verbose_name=u'Дата последней модификации ручная',
                                      blank=True,
                                      null=True,)
    lastmod_use_manual = models.BooleanField(verbose_name=u'Использовать указанную вручную дату последнего изменения',
                                             default=False,)
    lastmod_disable = models.BooleanField(verbose_name=u'Отключить указание lastmod',
                                          default=False,)

    priority = models.DecimalField(max_digits=3,
                                   decimal_places=2,
                                   verbose_name=u'Приоритет',
                                   default=Decimal(0.5),
                                   help_text=u'Стандартом sitemap.xml предусмотрено значение от 0.0 до 1.0',
                                   )
    priority_disable = models.BooleanField(verbose_name=u'Отключить указание Приоритета',
                                           default=False,)

    CHANGEFREQS = (
        ('always',u'постоянно'),
        ('hourly',u'каждый час'),
        ('daily',u'каждый день'),
        ('weekly',u'каждую неделю'),
        ('monthly',u'каждый месяц'),
        ('yearly',u'каждый год'),
        ('never',u'никогда'),
    )

    changefreq = models.CharField(verbose_name=u'Вероятная частота изменения этой страницы',
                                  choices=CHANGEFREQS,
                                  max_length=255,
                                  blank=True,
                                  null=True,
                                  default='weekly',
                                  )
    changefreq_disable = models.BooleanField(verbose_name=u'Отключить указание Приоритета',
                                             default=False,)

    order_num = models.IntegerField(verbose_name=u'Порядок отображения',
                                    default=50,)
    item_disable = models.BooleanField(verbose_name=u'Отключить объект в карте сайта',
                                       default=False,)
    item_id = models.PositiveIntegerField(verbose_name=u'Идентификатор объекта')

    item_model = models.ForeignKey(ContentType, verbose_name=u'Идентификатор модели')
    objects = SiteXmlManager()

    def get_priority(self):
        return '%s'.replace(',','.')%self.priority

    def get_absolute_url(self):
        obj = self.item_model.get_object_for_this_type(pk=self.item_id)
        return obj.get_absolute_url().strip()

    def __unicode__(self):
        return u''

    class Meta:
        verbose_name = u'элемент в карте сайта'
        verbose_name_plural = u'Карта сайта'


def delete_time(sender, instance, **kwargs):
    if sender.__name__ not in ['LogEntry','BasicMetadata','BasicSitemapData','Session']:
        for item in BasicSitemapData.objects.filter(page=instance):
            item.delete()
pre_delete.connect(delete_time)
