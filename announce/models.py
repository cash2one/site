# -*- coding: utf-8 -*-
import os

from django.db import models
from django.db.models.signals import post_delete
from pytils.translit import slugify
from pyadmin import verbose_name_cases
from PIL import Image
import datetime


class Announce(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'Заголовок', blank=True, null=True)
    created_at = models.DateField(verbose_name=u'Дата создания', default=datetime.date.today)
    slug = models.SlugField(verbose_name=u"Slug",
                            max_length=100, blank=True,
                            help_text=u'url, может содержать буквы, цифры, знак подчеркивания и дефис')
    is_visible_on_main = models.BooleanField(verbose_name=u'Показывать маячок у пункта в меню', default=False)
    is_visible_inner = models.BooleanField(verbose_name=u'Отображать на внутренних страницах', default=False)
    is_visible = models.BooleanField(verbose_name=u'Отображать', default=True)
    image = models.ImageField(verbose_name=u'Изображение, отображаемое в списке акций', blank=True,
                              upload_to='upload/announce',
                              help_text=u"<p>Изображение .jpg, jpeg, <strong>212x212</strong> px. <br>"
                                        u"Изображения с большим размером будут уменьшены с соблюдением пропорций </p>")
    teaser = models.TextField(help_text=u'Краткое описание акции', max_length=255, verbose_name=u'Краткое описание',
                              blank=True)
    description = models.TextField(help_text=u'Полный текст акции', verbose_name=u'Текст')
    order = models.IntegerField(verbose_name=u'Порядок отображения', default=0)

    @models.permalink
    def get_absolute_url(self):
        return 'announce:announce-detail', (), {'slug': self.slug}

    def __unicode__(self):
        return u'Акция №%s от %s' % (self.id, self.created_at)

    def got_image(self):
        try:
            if self.image:
                img_file = self.image.file
                if os.path.isfile(unicode(img_file)):
                    return True
        except:
            return False

    class Meta:
        verbose_name = verbose_name_cases(
            u'акция', (u'акции', u'акции', u'акции'),
            gender=0, change=u'акцию', delete=u'акцию', add=u'акцию'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('-created_at',)

    def save(self, *args, **kwargs):
        if self.title and not self.slug:
            self.slug = slugify(self.title)
            item = Announce.objects.filter(slug=self.slug)
            if item:
                self.slug += "_" + str(self.pk)

        super(Announce, self).save(*args, **kwargs)


def delete_metadata(sender, instance, **kwargs):
    try:
        from simpleseo.models import BasicMetadata
        BasicMetadata.objects.get(page=instance).delete()
    except:
        pass


post_delete.connect(delete_metadata, Announce)
