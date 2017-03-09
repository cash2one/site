# coding=utf-8
from django.db import models
from pyadmin import verbose_name_cases


class MapPoint(models.Model):
    TYPES_OF_POINT = (
        ('default', u'по-умолчанию'),
    )
    name = models.CharField(
        verbose_name=u'Название точки',
        max_length=255,)

    type_of_point = models.CharField(
        choices=TYPES_OF_POINT,
        max_length=255,
        verbose_name=u'Тип точки',
        default=TYPES_OF_POINT[0][0]
    )



    content = models.TextField(
        verbose_name=u'Контент',
        max_length=1000,
        blank=True,
    )

    image = models.ImageField(
        verbose_name=u'Изображение',
        blank=True,
        upload_to='upload/mapelements/',
        help_text=u'<p>Изображение .jpeg,jpg'
    )

    is_visible = models.BooleanField(
        default=True,
        verbose_name=u'Отображать?')

    address = models.CharField(
        verbose_name=u'Адрес',
        max_length=255,
        blank=True
    )

    coordinates = models.CharField(
        max_length=100,
        verbose_name=u'Координаты',
        blank=True
    )

    def __unicode__(self):
        return u'%s'% self.name

    class Meta:
        verbose_name = verbose_name_cases(
            u'элемент на карте', (u'элементы на карте', u'элементы на карте', u'эелемнты на карте'),
            gender=1, change=u'элемент на карте', delete=u'элемент на карте', add=u'элемент на карте'
        )
        verbose_name_plural = verbose_name.plural