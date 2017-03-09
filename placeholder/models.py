# -*- coding: utf-8 -*-

from django.db import models
from django.utils.safestring import mark_safe
from pyadmin import verbose_name_cases
from django.template.defaultfilters import linebreaksbr

PLACEHOLDERS = (
    ('header_phone1', u'Телефон в шапке 1'),
    ('header_phone2', u'Телефон в шапке 2'),
    ('footer_1', u'Блок в футере 1'),
    ('footer_2', u'Блок в футере 2'),
    ('footer_3', u'Блок в футере 3'),
    ('footer_4', u'Блок в футере 4'),
    ('requisites', u'Блок реквизитов на странице конткатов')
    # ('email', u'E-mail'),
    # ('address', u'адрес'),
)

class Placeholder(models.Model):
    TEMPLATES = (
        ("phone_mobile", u"мобильный"),
        # ("phone_city", u"городской")
        ("email", u"E-mail"),
        ("skype", u"skype"),
        ("address", u"адрес"),
        ("phone", u"Телефон"),
        ("html", u"Визуальный редактор")
    )

    name = models.CharField(
        verbose_name=u'Название',
        help_text=u'Уникальное название блока',
        max_length=255,
        unique=True,
        choices=PLACEHOLDERS)

    template = models.CharField(
        verbose_name=u'Шаблон',
        help_text=u'',
        max_length=255,
        choices=TEMPLATES,
        blank=True)

    source_content = models.TextField(
        verbose_name=u'Содержимое',
        blank=True
    )

    content = models.TextField(
        verbose_name=u'Содержимое',
        blank=True
    )

    def __unicode__(self):
        return u'%s' % (self.name,)

    def save(self, *args, **kwargs):
        src = self.source_content
        if src:
            tmpl = self.template
            if "footer_" in self.name:
                blok_start = u'<div class="col-xs-12 col-sm-6 col-md-3 contact-info-item">'
                blok_end = u'</div>'
                if tmpl == "html":
                    self.content = blok_start + src + blok_end
                else:
                    blok_title = u'<h4>%s</h4>' % next((i[1] for i in self.TEMPLATES if i[0] == self.template), "")
                    if tmpl == "email":
                        content = u'<a href="mailto:%s">%s</a>' % (src, src)
                    elif tmpl == "skype":
                        content = u'<a href="skype:%s">%s</a>' % (src, src)
                    else:
                        content = src
                    self.content = blok_start + blok_title + u"<p>%s</p>" % linebreaksbr(content) + blok_end
            else:
                if tmpl == "phone_mobile":
                    self.content = u'<a href="tel:%s"class="header-phone">' \
                                   u'<span class="phone-code">%s</span> <strong>%s</strong>' \
                                   u'</a>' % (src, src[:7], src[7:])
                if tmpl == "html":
                    self.content = src
        else:
            self.content = src
        super(Placeholder, self).save(*args, **kwargs)

    class Meta:
        verbose_name = verbose_name_cases(
            u'Горячие контакты', (
                u'Горячие контакты',
                u'элементы горячих контактов',
                u'элементы горячих контактов'
            ),
            gender=1,
            change=u'элемент горячих контактов',
            delete=u'элемент горячих контактов',
            add=u'элемент горячих контактов'
        )
        verbose_name_plural = verbose_name.plural

