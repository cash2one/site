# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse

from addressprogram.models import AdvertisingSpace
from django.contrib.contenttypes.models import ContentType, ContentTypeManager
from django.db import models
from django.db.models import permalink
from pyadmin import verbose_name_cases
from feedback.forms import validate_phone


class AdminURLMixin(object):
    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return reverse("admin:%s_%s_change" % (
            content_type.app_label,
            content_type.model),
                       args=(self.id,))


class Cart(models.Model):
    created_at = models.DateTimeField(verbose_name=u'Дата создания')
    is_checked_out = models.BooleanField(verbose_name=u'Заказ сформирован', default=False)

    class Meta:
        verbose_name = verbose_name_cases(
            u'корзина', (u'корзины', u'корзины', u'корзины'),
            gender=0, change=u'корзину', delete=u'корзину', add=u'корзину'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('-created_at',)

    def __unicode__(self):
        return unicode(self.created_at)


class CartItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'item' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['item']))
            kwargs['object_id'] = kwargs['item'].pk
            del (kwargs['item'])
        return super(CartItemManager, self).get(*args, **kwargs)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=u'Корзина')
    grp = models.CharField(verbose_name=u'Рейтинг поверхности', max_length=255, blank=True)
    ots = models.CharField(verbose_name=u'OTS', max_length=255, blank=True)
    quantity = models.PositiveIntegerField(verbose_name=u'Количество', default=1, editable=False)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    objects = ContentTypeManager()

    class Meta:
        verbose_name = verbose_name_cases(
            u'элемент корзины', (u'Элементы корзины', u'элементы корзины', u'элементов корзины'),
            gender=2, change=u'элемент корзины', delete=u'элемент корзины', add=u'элемент корзины'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('cart',)

    def __unicode__(self):
        return self.product.address.address

    def total_grp(self):
        if not self.grp == u'н/д':
            return float(self.grp.replace(',', '.').encode().strip())
        else:
            self.grp = 0
            return self.grp

    total_grp = property(total_grp)

    def get_item(self):
        return self.content_type.get_object_for_this_type(id=self.object_id)

    def set_item(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_item, set_item)


class OrderStatus(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=255)
    is_initial = models.BooleanField(verbose_name=u'Начальный', default=False)
    is_closing = models.BooleanField(verbose_name=u'Конечный', default=False)
    index_number = models.IntegerField(verbose_name=u'Порядок статуса', default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_cases(
            u'статус заказа', (u'статус заказа', u'статус заказа', u'статус заказа'),
            gender=2, change=u'Статусы заказов', delete=u'Статусы заказов', add=u'Статусы заказов'
        )
        verbose_name_plural = verbose_name.plural


class Order(models.Model, AdminURLMixin):
    ip = models.IPAddressField(verbose_name=u'IP-адрес', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name=u'Дата оформления', auto_now_add=True, blank=True, null=True)
    full_name = models.CharField(verbose_name=u'Ф.И.О.', max_length=255, blank=True)
    company = models.CharField(verbose_name=u"Компания", max_length=500, blank=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length=255, blank=True)
    email = models.EmailField(verbose_name=u'E-mail', blank=True)
    status = models.ForeignKey(OrderStatus, verbose_name=u'Статус', blank=True, null=True)
    date_start = models.DateField(verbose_name=u'Дата начала размежиния', blank=True, null=True)
    date_end = models.DateField(verbose_name=u'Дата окончания размещения', blank=True, null=True)

    class Meta:
        verbose_name = verbose_name_cases(
            u'заказ', (u'Заказ', u'Заказ', u'Заказ'),
            gender=2, change=u'Заказ', delete=u'Заказ', add=u'Заказ'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('-created_at',)

    def __unicode__(self):
        return u'Заказ №%s от %s' % (self.id, self.created_at)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=u'Заказ')
    passport = models.ForeignKey(AdvertisingSpace, verbose_name=u'Товар', on_delete=models.SET_NULL, null=True)
    grp = models.CharField(verbose_name=u'Рейтинг поверхности', max_length=255, blank=True)
    ots = models.CharField(verbose_name=u'OTS', max_length=255, blank=True)
    quantity = models.SmallIntegerField(verbose_name=u'Количество', blank=True, editable=False, default=1)

    # save product name in case it would be delete by carefree admin
    passport_name = models.CharField(verbose_name=u'Наименование товара', max_length=255, blank=True)

    class Meta:
        verbose_name = verbose_name_cases(
            u'Элемент заказа', (u'Элементы заказов', u'Элементы заказов', u'Элементы заказов'),
            gender=1, change=u'Элемент заказа', delete=u'Элемент заказа', add=u'Элемент заказа'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('order',)

    def get_absolute_url(self):
        return self.passport.get_absolute_url()

    def save(self, *args, **kwargs):
        if not self.passport_name and self.passport:
            self.passport_name = self.passport.address.address
        super(OrderItem, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'Позиция заказа №%s. Наименование: %s, Количество: %s' % \
               (self.order.id, self.passport_name, self.quantity)
