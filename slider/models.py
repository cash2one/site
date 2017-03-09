# -*- coding: utf-8 -*-

from django.db import models
from pyadmin import verbose_name_cases
import os

class Slide(models.Model):
    name = models.CharField(max_length=255, verbose_name=u'Название')
    url = models.CharField(
        verbose_name=u'URL',
        blank=True,
        null=True,
        max_length=255,
        help_text=u"<p>Если заполнено - на слайд добавляется кнопка,<br> "
                  u"при клике на которую будет происходить переход по указанной ссылке</p>"
    )

    content = models.TextField(verbose_name=u'Контент слайда',blank=True,null=True)
    image = models.ImageField(
        verbose_name=u'Изображение',
        blank=True,
        upload_to='upload/slider/',
        help_text=u'<p>Изображение .jpeg,jpg c размерами <strong>1440x530</strong>,<br> '
                  u'изображение большего размера будет уменьшено и обрезано,<br>'
                  u'изображение меньшего размера использовать не рекомендуется</p>'
    )
    order = models.SmallIntegerField(verbose_name=u'Порядок отображения', default=0)
    show = models.BooleanField(verbose_name=u'Отображать?',default=True)


    def __unicode__(self):
        return '%s' % self.name

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
            u'слайд', (u'Слайды', u'слайды', u'слайдов'),
            gender = 0, change = u'слайд', delete = u'слайд', add = u'слайд'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('order',)
