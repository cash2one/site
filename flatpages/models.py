# -*- coding: utf-8 -*-
import os
from django.core.urlresolvers import reverse

from django.db import models
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager
from mptt.models import MPTTModel
from django.db.models.signals import post_delete, post_save

from announce.models import Announce
from pyadmin import verbose_name_cases


class FlatPage(MPTTModel):
    TYPES = (
        ('text', u'Текстовая'),
        ('news', u'Новости'),
        ('announce', u'Анонсы'),
        ('contacts', u'Контакты'),
        ('program', u'Адресная программа'),
        ('requirements', u'Tex. требования(список продуктов)')
    )

    parent = TreeForeignKey(
        'self',
        related_name='child',
        verbose_name=u'Родительская страница',
        blank=True,
        null=True
    )

    title = models.CharField(
        u'Заголовок',
        max_length=200
    )

    url = models.CharField(
        verbose_name=u'URL',
        help_text=u'Если указать урл на новость или анонс то данный элемент в меню будет ссылкой',
        max_length=100,
        db_index=True,
        unique=True
    )

    content = models.TextField(
        u'Cодержимое страницы',
        blank=True
    )

    menu_title = models.CharField(
        max_length=255,
        verbose_name=u'Заголовок в меню',
        blank=True,
        null=True,
        help_text=u'Пустое поле будет означать дублирование заголовка страницы'
    )

    type = models.CharField(
        verbose_name=u'Тип',
        help_text=u'Характеризует функционал страницы',
        max_length=255,
        choices=TYPES,
        default='text',
    )

    show_in_menu = models.BooleanField(
        default=False,
        verbose_name=u'Отображать в верхнем меню'
    )

    show_in_side_menu = models.BooleanField(
        default=False,
        verbose_name=u'Отображать в боковом меню'
    )

    is_visible = models.BooleanField(
        default=True,
        verbose_name=u'Отображать?'
    )

    tree = TreeManager()

    order = models.SmallIntegerField(
        verbose_name=u'Порядок отображения',
        default=0
    )

    class MPTTMeta:
        parent_attr = 'parent'
        order_insertion_by = 'order'

    class Meta:
        verbose_name = verbose_name_cases(
            u'элемент сайта', (
                u'дерево сайта',
                u'элементы сайта',
                u'элементов сайта'
            ),
            gender=2,
            change=u'элемент',
            delete=u'элемент',
            add=u'элемент'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('url',)

    def __unicode__(self):
        return u"%s" % self.title

    def __str__(self):
        return u"%s" % self.title

    def get_title(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        url = self.url
        if url.startswith('/'):
            url = url[1:]
        return 'fpc:flatpage-det', (), {'url': url}

    def get_breadcrumbs(self):
        breadcrumbs = []
        for ancestor in self.get_ancestors(include_self=True):
            if ancestor.menu_title:
                ancestor.name = ancestor.menu_title
            else:
                ancestor.name = ancestor.title
            breadcrumbs.append(ancestor)
        return breadcrumbs

    def save(self, *args, **kwargs):
        if not self.url.startswith('/'):
            self.url = '/' + self.url
        if not self.url.endswith('/'):
            self.url += '/'
        if self.type == 'news':
            self.url = reverse("news:news-list")
        if self.type == 'requirements':
            self.url = reverse("program:construction-list")
        if self.type == 'announce':
            self.url = reverse("announce:announce-list")
        super(FlatPage, self).save(*args, **kwargs)

    def get_top_menu_children(self):
        return self.get_children().filter(is_visible=True, show_in_menu=True)

    def get_menu_title(self):
        if self.menu_title:
            return self.menu_title
        return self.title

    def get_announce_count(self):
        if self.type == 'announce':
            announces = Announce.objects.filter(is_visible=True, is_visible_on_main=True).count()
            return announces


def save_fp(sender, instance, **kwargs):
    FlatPage.tree.rebuild()


post_save.connect(save_fp, FlatPage)
post_delete.connect(save_fp, FlatPage)


class IndexPage(models.Model):
    content = models.TextField(
        verbose_name=u"Текст в блоке 'Почему мы?'",
        blank=True,
        null=True
    )

    def __unicode__(self):
        return u"%s" % u"Текст в блоке 'Почему мы?'"

    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = verbose_name_cases(
            u"Текст в блоке 'Почему мы?'", (
                u"Текст в блоке 'Почему мы?'",
                u"Тексты в блоке 'Почему мы?'",
                u"Текстов в блоке 'Почему мы?'"
            ),
            gender=1,
            change=u"Текст в блоке 'Почему мы?'",
            delete=u"Текст в блоке 'Почему мы?'",
            add=u"Текст в блоке 'Почему мы?'"
        )
        verbose_name_plural = verbose_name.plural


# Тут стандартно. удаляем
def delete_metadata(sender, instance, **kwargs):
    try:
        from simpleseo.models import BasicMetadata

        BasicMetadata.objects.get(page=instance).delete()
    except:
        pass


post_delete.connect(delete_metadata, FlatPage)
post_delete.connect(delete_metadata, IndexPage)


class IndexAbout(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=u'Заголовок',
        blank=True
    )
    left_content = models.TextField(
        verbose_name=u'Левая колонка',
        blank=True,
    )
    right_content = models.TextField(
        verbose_name=u'Правая колонка',
        blank=True,
    )

    def __unicode__(self):
        if self.title:
            return u"Текст в блоке '%s'" % self.title
        else:
            return u'Текст N%s' % self.id

    def get_absolute_url(self):
        return '/'

    class Meta:
        verbose_name = verbose_name_cases(
            u"Текст в блоке 'О компании'", (
                u"Текст в блоке 'О компании'",
                u"Тексты в блоке 'О компании'",
                u"Текстов в блоке 'О компании'"
            ),
            gender=1,
            change=u"Текст в блоке 'О компании'",
            delete=u"Текст в блоке 'О компании'",
            add=u"Текст в блоке 'О компании'"
        )
        verbose_name_plural = verbose_name.plural


# Тут стандартно. удаляем
def delete_metadata(sender, instance, **kwargs):
    try:
        from simpleseo.models import BasicMetadata

        BasicMetadata.objects.get(page=instance).delete()
    except:
        pass


post_delete.connect(delete_metadata, IndexAbout)


class Advantage(models.Model):
    content = models.TextField(
        verbose_name=u'Текст преимущества',
        blank=True,
        null=True
    )

    image = models.ImageField(
        verbose_name=u'Изображение',
        blank=True,
        upload_to='upload/advantages/',
        help_text=u'<p>Изображение jpeg/png c размерами <strong>128x128</strong> px<br>'
                  u'изображение большего размера будет уменьшено c сохранением пропорций и обрезано,<br>'
                  u'изображение меньше указанного размера изменено</p>'
    )

    order = models.SmallIntegerField(
        verbose_name=u'Порядок отображения',
        default=0
    )

    show = models.BooleanField(
        verbose_name=u'Отображать?',
        default=True
    )

    def __unicode__(self):
        if self.content:
            return u'%s' % self.content
        else:
            return u'Преимущество %s' % self.id

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
            u'Преимущество', (u'Преимущество', u'Преимущества', u'Преимуществ'),
            gender=0, change=u'преимущество', delete=u'преимущество', add=u'преимущество'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('order',)


class Manager(models.Model):
    full_name = models.CharField(
        verbose_name=u'Сотрудник',
        max_length=100,
        blank=True,
        null=True,
        help_text=u'Петрова Анастасия'
    )

    man_image = models.ImageField(
        verbose_name=u'Фото',
        blank=True,
        upload_to='upload/manager/',
        help_text=u'<p>Изображение jpeg/png c размерами <strong>180x180</strong> px<br>'
                  u'изображение большего размера будет уменьшено c сохранением пропорций и обрезано,<br>'
                  u'изображение меньше указанного размера изменено</p>'
    )

    position = models.CharField(
        verbose_name=u'Должность',
        max_length=100,
        blank=True,
        null=True
    )

    email = models.EmailField(
        verbose_name=u'E-mail',
        blank=True
    )

    sub_email = models.EmailField(
        verbose_name=u'Дополнительный E-mail',
        blank=True
    )

    order = models.SmallIntegerField(
        verbose_name=u'Порядок отображения',
        default=0
    )

    show = models.BooleanField(
        verbose_name=u'Отображать',
        default=True
    )

    def __unicode__(self):
        if self.full_name:
            return u'%s' % self.full_name
        else:
            return u'Менеджер N%s' % self.id

    def get_image_url(self):
        if self.man_image and hasattr(self.man_image, 'url'):
            return self.man_image.url
        else:
            return '/media/images/logo.png'

    class Meta:
        verbose_name = verbose_name_cases(
            u'Менеджер', (u'Менеджеры', u'Менеджера', u'Менеджеров'),
            gender=1, change=u'Менеджера', delete=u'Менеджера', add=u'Менеджера'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('order',)
