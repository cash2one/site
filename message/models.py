# -*- coding: utf8 -*-

from django.db import models
from tinymce import models as tinymce_models
from pyadmin import verbose_name_cases


class Message(models.Model):
    CHOICES = (
        ('message_after_feedback_form', u'После успешной отправки формы обратной связи на странице контактов'),
        ('message_after_adding_the_goods_into_the_basket', u'После добавления товара в корзину'),
        ('message_after_successful_order', u'После успешного оформления заказа'),

    )

    type = models.CharField(choices=CHOICES, max_length=255, verbose_name=u'Тип', unique=True)
    message = models.TextField(verbose_name=u'Текст сообщения', blank = True)

    def __unicode__(self):
        return self.get_type_display()

    def get_absolute_url(self):
        return u"/kontakty/?thanks_for_feedback=true"

    class Meta:
        verbose_name = verbose_name_cases(
            u'уведомление на сайте', (u'уведомление на сайте', u'уведомления на сайте', u'уведомлений на сайте'),
            gender = 0, change = u'уведомление на сайте', delete = u'уведомление на сайте', add = u'уведомление на сайте'
        )
        verbose_name_plural = verbose_name.plural


class Mail(models.Model):
    CHOICES = (
        ('contacts_email', u'Письмо со страницы контактов'),
        ('manager_email', u'Письмо со страницы контактов менеджеру'),
        ('seller_email', u'Письмо менеджеру после оформления заказа'),
        ('customer_email', u'Письмо покупателю после оформления заказа'),
        )

    type = models.CharField(choices=CHOICES, max_length=255, verbose_name=u'Тип', unique=True)
    subject = models.CharField(max_length=255, verbose_name=u'Тема письма', blank=True, null=True)
    mail = tinymce_models.HTMLField(verbose_name=u'Текст письма', blank=True)

    def __unicode__(self):
        return self.get_type_display()

    class Meta:
        verbose_name = verbose_name_cases(
            u'уведомление на почту', (u'уведомление на почту', u'уведомления на почту', u'уведомлений на почту'),
            gender = 0, change = u'уведомление на почту', delete = u'уведомление на почту', add = u'уведомление на почту'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('type',)
