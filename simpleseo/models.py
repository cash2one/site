# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.db import models
from flatpages.models import FlatPage
from pyadmin import verbose_name_cases
from django.db.models.signals import pre_delete

class SeoManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'page' in kwargs:
            kwargs['item_model'] = ContentType.objects.get_for_model(type(kwargs['page']))
            kwargs['item_id'] = kwargs['page'].pk
            del (kwargs['page'])
        return super(SeoManager, self).get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        if 'page' in kwargs:
            kwargs['item_model'] = ContentType.objects.get_for_model(type(kwargs['page']))
            kwargs['item_id'] = kwargs['page'].pk
            del (kwargs['page'])
        return super(SeoManager, self).filter(*args, **kwargs)


class BasicMetadata(models.Model):
    title = models.TextField(blank=True, null=True, verbose_name=u'title')
    description = models.TextField(blank=True, null=True, verbose_name=u'description')
    keywords = models.TextField(blank=True, null=True, verbose_name=u'keywords')
    item_id = models.PositiveIntegerField(verbose_name=u'Идентификатор объекта')
    item_model = models.ForeignKey(ContentType, verbose_name=u'Идентификатор модели')
    objects = SeoManager()

    def __unicode__(self):
        return u''

    def save(self, *args, **kwargs):
        item = self.item_model.model_class().objects.get(id=self.item_id)

        try:
            if len(self.title) == 0:
                if self.item_model.model_class() == FlatPage:
                    title = item.title
                else:
                    title = item.__unicode__()
                self.title = title
        except:
            pass
        super(BasicMetadata, self).save(*args, **kwargs)


    class Meta:
        verbose_name = verbose_name_cases(
            u'SEO', (u'SEO', u'SEO', u'SEO'),
            gender = 0, change = u'SEO', delete = u'SEO', add = u'SEO'
        )
        verbose_name_plural = verbose_name.plural

def delete_time(sender, instance, **kwargs):
    if sender.__name__ not in ['LogEntry','BasicMetadata','BasicSitemapData','Session']:
        for item in BasicMetadata.objects.filter(page=instance):
            item.delete()
pre_delete.connect(delete_time)
