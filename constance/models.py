# coding=utf-8
from django.db import models
from picklefield import PickledObjectField
from pyadmin import verbose_name_cases


class Config(models.Model):
    key = models.CharField(verbose_name=u'Тип', max_length=255, unique=True)
    value = PickledObjectField()

    def __unicode__(self):
        return u'%s - %s' % (self.key, self.value)

    @classmethod
    def get_by_key(cls, key):
        return cls.objects.get(key=key).value

    class Meta:
        verbose_name = verbose_name_cases(
            u'константы', (u'константы', u'', u'текстов серверных ошибок'),
            gender=1, change=u'текст серверных ошибок', delete=u'текст серверных ошибок', add=u'текст серверных ошибок'
        )
        verbose_name_plural = verbose_name.plural