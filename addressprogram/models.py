# coding=utf-8
import os

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from pytils.translit import slugify
from django.db.models.signals import post_save

from main.settings import MEDIA_URL, MEDIA_ROOT
from pyadmin import verbose_name_cases


class Region(models.Model):
    date = models.DateTimeField(verbose_name=u'Дата создания', default=timezone.now())
    name = models.CharField(verbose_name=u'Название региона', max_length=255)
    slug = models.SlugField(verbose_name=u'Slug', max_length=100, blank=True,
                            help_text=u'URL, может содержать буквы, цифры, знак подчеркивания и дефис')
    is_visible = models.BooleanField(verbose_name=u'Отображать', default=True)

    class Meta:
        verbose_name = verbose_name_cases(
            u'Регион', (u'Регионы', u'Региона', u'Регионов'),
            gender=1, change=u'Регион', delete=u'Регион', add=u'Регион'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('-date',)

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
            item = Region.objects.filter(slug=self.slug)
            if item:
                self.slug += "_" + str(self.pk)

        super(Region, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class City(models.Model):
    date = models.DateTimeField(verbose_name=u'Дата создания', default=timezone.now())
    name = models.CharField(verbose_name=u'Название', max_length=50)
    slug = models.SlugField(verbose_name=u'Slug', max_length=50, blank=True,
                            help_text=u'URL, может содержать буквы, цифры, знак подчеркивания и дефис')

    emblem = models.ImageField(verbose_name=u'Герб', upload_to='uploads/addressprogram/city/',
                               help_text=u'Минимальный размер изображения 213px х 254px(h)')
    region = models.ForeignKey(Region, verbose_name=u'Округ')
    population = models.CharField(verbose_name=u'Население', max_length=50, help_text=u'образец: "**** тысяч человек"')
    transport = models.CharField(verbose_name=u'Транспорт', max_length=100,
                                 help_text=u'образец: "жд.вокзал, автовокзалы, аэропорт"')
    status = models.CharField(verbose_name=u'Статус', max_length=100,
                              help_text=u'образец: "Административный центр Челябинской области"', blank=True, null=True)
    area = models.CharField(verbose_name=u'Площадь', max_length=50, help_text=u'образец: "**** км2"')
    based = models.CharField(verbose_name=u'Основан', max_length=50, help_text=u'образец: "в **** году."', blank=True,
                             null=True)
    distance = models.CharField(verbose_name=u'Расстояние до областного центра', max_length=50,
                                help_text=u'Расстояние до областного центра: 260 км', blank=True, null=True)
    description = models.TextField(verbose_name=u'Описание', blank=True, null=True)
    site = models.URLField(verbose_name=u'Сайт', blank=True)
    order = models.SmallIntegerField(verbose_name=u'Порядок', default=0)
    is_visible = models.BooleanField(verbose_name=u'Отображать', default=True)

    available_constructions = models.ManyToManyField(
        'Construction',
        verbose_name=u"available_constructions",
        blank=True
    )

    class Meta:
        verbose_name = verbose_name_cases(
            u'Город', (u'Города', u'Города', u'Городов'),
            gender=1, change=u'Город', delete=u'Город', add=u'Город'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('order',)

    def __unicode__(self):
        return self.name

    def get_available_constructions(self):
        return self.available_constructions.all()

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
            item = Region.objects.filter(slug=self.slug)
            if item:
                self.slug += "_" + str(self.pk)

        super(City, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'program:city_detail', (), {'slug': self.slug}

    def get_image_url(self):
        if self.emblem and hasattr(self.emblem, 'url'):
            return self.emblem.url
        else:
            return '/media/images/logo.png'


class Construction(models.Model):
    date = models.DateTimeField(verbose_name=u'Дата создания', default=timezone.now())
    name = models.CharField(verbose_name=u'Название', max_length=100)
    icon = models.ImageField(verbose_name=u'Иконка', upload_to='uploads/addressprogram/construction/',
                             help_text=u'Минимальный размер изображения 213px х 254px(h)',
                             default='/media/images/logo.png')
    icon_hover = models.ImageField(verbose_name=u'Иконка(при наведение)', upload_to='uploads/addressprogram/construction/',
                             help_text=u'Минимальный размер изображения 213px х 254px(h)',
                             default='/media/images/logo.png')
    icon_active = models.ImageField(verbose_name=u'Иконка(при нажатии)', upload_to='uploads/addressprogram/construction/',
                             help_text=u'Минимальный размер изображения 213px х 254px(h)',
                             default='/media/images/logo.png')
    marker_icon = models.ImageField(verbose_name=u'Иконка для маркера',
                                    upload_to='uploads/addressprogram/construction/',
                                    help_text=u'Минимальный размер изображения 24px х 25px(h)',
                                    default='/media/images/type1.png')
    marker_icon_active = models.ImageField(verbose_name=u'Иконка для маркера(активная)',
                                           upload_to='uploads/addressprogram/construction/',
                                           help_text=u'Минимальный размер изображения 24px х 25px(h)',
                                           default='/media/images/type1-active.png')
    # TODO уточнить размер загружаемой картинки
    short_content = models.TextField(verbose_name=u'Краткое описание', blank=True)
    order = models.SmallIntegerField(verbose_name=u'Порядок', default=0)
    show = models.BooleanField(verbose_name=u'Отображать?', default=True)
    show_in_main = models.BooleanField(verbose_name=u'Отображать на главной', default=True)
    show_footer = models.BooleanField(verbose_name=u'Отображать в футере', default=True)
    show_in_city = models.BooleanField(verbose_name=u'Отображать на странице города', default=True)
    content = models.TextField(verbose_name=u'Описание', blank=True)
    slug = models.SlugField(verbose_name=u'Slug', max_length=100, blank=True)

    class Meta:
        verbose_name = verbose_name_cases(
            u'Продукт', (u'Продукты', u'Продуктов', u'Продуктов'),
            gender=1, change=u'Продукт', delete=u'Продукт', add=u'Продукт'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('order',)

    @models.permalink
    def get_absolute_url(self):
        return 'program:construction-detail', (), {'slug': self.slug}

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name and not self.slug:
            self.slug = slugify(self.name)
            item = Construction.objects.filter(slug=self.slug)
            if item:
                self.slug += "_" + str(self.pk)
        super(Construction, self).save(*args, **kwargs)

    def get_icon_url(self):
        if self.icon and hasattr(self.icon, 'url'):
            return self.icon.url
        else:
            return '/media/images/logo.png'


class GeoObject(models.Model):
    date = models.DateTimeField(verbose_name=u'Дата создания', default=timezone.now())
    city = models.ForeignKey(City, verbose_name=u'Город')
    prod = models.ForeignKey(Construction, verbose_name=u'Продукт', default=1)

    is_visible = models.BooleanField(verbose_name=u'Отображать', default=True)
    construction = models.CharField(max_length=50, verbose_name=u'Продукт', blank=True)
    address = models.CharField(verbose_name=u'Адрес', max_length=255,
                               help_text=u'образец: 1 - й Пятилетки ул. - ул. Артиллерийская ')
    coordinates = models.CharField(
        max_length=100,
        verbose_name=u'Координаты',
        blank=True
    )

    latitude = models.CharField(verbose_name=u'Широта', max_length=10, help_text=u'00.000000')
    longitude = models.CharField(verbose_name=u'Долгота', max_length=10, help_text=u'00.000000')

    class Meta:
        verbose_name = verbose_name_cases(
            u'Объект', (u'Объекты', u'Объекта', u'Объектов'),
            gender=1, change=u'Объект', delete=u'Объект', add=u'Объект'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('address',)

    def __unicode__(self):
        return self.address


class AdvertisingSpace(models.Model):
    PRINT_URL_BASE = os.path.join(MEDIA_URL, 'screenshots')
    CHOICE_BACKLIGHT = (
        ('yes', u'Да'),
        ('no', u'Нет')
    )
    date = models.DateTimeField(verbose_name=u'Дата создания', default=timezone.now())
    address = models.ForeignKey(GeoObject, verbose_name=u'Адрес')
    description = models.CharField(verbose_name=u'Описание', max_length=255, help_text=u'****сторонняя конструкция',
                                   blank=True, null=True)
    type = models.ForeignKey(Construction, verbose_name=u'Тип')
    side = models.CharField(verbose_name=
                            u'Сторона', max_length=255, help_text=u'Указать сторону А, B, C ...')
    backlight = models.CharField(verbose_name=u'Подсветка', choices=CHOICE_BACKLIGHT, default='yes', max_length=5)
    gid = models.CharField(verbose_name=u'GID', max_length=100, blank=True, null=True)
    grp = models.CharField(verbose_name=u'Коэффициент GRP', max_length=50, blank=True, null=True)
    ots = models.CharField(verbose_name=u'OTS', max_length=50, blank=True, null=True)
    size = models.CharField(verbose_name=u'Формат', max_length=100, blank=True, null=True)
    material = models.TextField(verbose_name=u'Материал', blank=True)
    scheme = models.ImageField(verbose_name=u'Схема', upload_to='uploads/addressprogram/adv_space/105/170/',
                               help_text=u'Минимальный размер изображения 400px х 260px(h)')
    is_visible = models.BooleanField(verbose_name=u'Отображать', default=True)
    has_print = models.BooleanField(verbose_name=u'has print', default=False)

    class Meta:
        verbose_name = verbose_name_cases(
            u'Паспорт', (u'паспорта', u'Паспорта', u'Паспортов'),
            gender=0, change=u'Паспорт', delete=u'Паспорт', add=u'Паспорт'
        )
        verbose_name_plural = verbose_name.plural
        ordering = ('address__address', 'side',)

    def __unicode__(self):
        return '%s %s' % (self.address.address, self.side)

    @models.permalink
    def get_absolute_url(self):
        return 'program:passport_detail', (), {'passport_id': self.id}

    @models.permalink
    def get_print_preview_url(self):
        return 'program:passport-print-preview', (), {'passport_id': self.id}

    def get_print_image_url(self):
        return os.path.join(MEDIA_URL, 'screenshots/print_%s.png' % self.id)

    def get_print_image_path(self):
        return os.path.join(MEDIA_ROOT, 'screenshots/print_%s.png' % self.id)

    def get_scheme_url(self):
        if self.scheme and hasattr(self.scheme, 'url'):
            return self.scheme.url

    def get_material_file(self):
        if self.material:
            return self.material

    def get_primary_image(self):
        images = Image.objects.filter(advertisingspace=self, is_primary=True)
        if images.exists():
            return images[0]
        return None

    def get_primary_image_url(self):
        images = Image.objects.filter(advertisingspace=self, is_primary=True)
        if images.exists():
            return images[0].file
        return None

    def get_images(self):
        return Image.objects.filter(advertisingspace=self, is_primary=False)

    def get_secondary_images(self):
        return Image.objects.filter(advertisingspace=self, is_primary=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None, from_printer=False):
        if from_printer:
            self.has_print = True
        else:
            self.has_print = False
        super(AdvertisingSpace, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


def update_city_available_constructions(*args, **kwargs):
    fields = kwargs.get('update_fields','none')
    constructions = AdvertisingSpace.objects.filter(address__city__is_visible=True).values_list(
        'address__city__id', 'type__id'
    )

    sorted_constructions = set(constructions)

    city_map = {}

    for i, k in sorted_constructions:
        if city_map.get(i):
            city_map[i].append(k)
        else:
            city_map[i] = [k]

    for cid, ccids in city_map.iteritems():
        city = City.objects.get(id=cid)
        city.available_constructions.clear()
        city.available_constructions.add(*Construction.objects.filter(id__in=ccids))
        city.save()


post_save.connect(receiver=update_city_available_constructions, sender=AdvertisingSpace)


class ImageManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'advertisingspace' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['advertisingspace']))
            kwargs['object_id'] = kwargs['advertisingspace'].pk
            del (kwargs['advertisingspace'])
        return super(ImageManager, self).get(*args, **kwargs)

    def get_or_create(self, *args, **kwargs):
        if 'advertisingspace' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['advertisingspace']))
            kwargs['object_id'] = kwargs['advertisingspace'].pk
            del (kwargs['advertisingspace'])
        return super(ImageManager, self).get_or_create(**kwargs)

    def filter(self, *args, **kwargs):
        if 'advertisingspace' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['advertisingspace']))
            kwargs['object_id'] = kwargs['advertisingspace'].pk
            del (kwargs['advertisingspace'])
        return super(ImageManager, self).filter(*args, **kwargs)


class Image(models.Model):
    file = models.ImageField(verbose_name=u'Файл', upload_to='uploads/addressprogram/adv_space/105/170/',
                             help_text=u'Минимальный размер изображения - 160x165 пикселей')
    name = models.CharField(max_length=255, verbose_name=u'Название', blank=True, null=True)
    is_primary = models.BooleanField(verbose_name=u'Основное изображение', default=False)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    objects = ImageManager()

    def __unicode__(self):
        return '%s' % self.name

    def get_item(self):
        return self.content_type.get_object_for_this_type(id=self.object_id)

    def set_item(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    item = property(get_item, set_item)

    def get_image_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url
        else:
            return '/media/images/logo.png'

    class Meta:
        verbose_name = verbose_name_cases(
            u'изображение', (u'изображения', u'изображения', u'изображения'),
            gender=1, change=u'изображение', delete=u'изображение', add=u'изображение'
        )
        verbose_name_plural = verbose_name.plural