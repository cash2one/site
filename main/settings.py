# -*- coding: utf-8 -*-

import os

ROOT = os.path.abspath(os.path.dirname(__file__))
path = lambda *args: os.path.join(ROOT, *args)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    (u'Никоненко Илья', 'iv@simplemedia.ru'),
    (u'Грин Тёма', 'tema@simplemedia.ru'),
)

MANAGERS = ADMINS

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'karus',
    #     'USER': 'karus',
    #     'PASSWORD': 'karus',
    #     'HOST': 'localhost',
    #     'PORT': '',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'karus',
        'USER': 'root',
        'PASSWORD': '111111',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

TIME_ZONE = 'Asia/Yekaterinburg'
LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

SITE_ID = 1

USE_I18N = True
USE_L10N = True
ALLOWED_HOSTS = [
    '.simplemedia.ru',  # Allow domain and subdomains
    '.simplemedia.ru.',  # Also allow FQDN and subdomains
]

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(PROJECT_ROOT, '..')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'

STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '*ywveerf_(v1v7bcx0!&x=8%1g$(ky&b-28+#c#z7chrm3x$ruidc'
SESSION_COOKIE_AGE = 365 * 24 * 60 * 60

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.static',
    'main.context_processors.current_site',
    'constance.context_processors.config',

)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'main.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'main.urls'

TEMPLATE_DIRS = ()
for root, dirs, files in os.walk(PROJECT_ROOT):
    if 'templates' in dirs: TEMPLATE_DIRS += (os.path.join(root, 'templates'),
                                              )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'sorl.thumbnail',
)

# grappelli, dashboard
INSTALLED_APPS = ('grappelli',) + INSTALLED_APPS
INSTALLED_APPS = ('grappelli.dashboard',) + INSTALLED_APPS
GRAPPELLI_INDEX_DASHBOARD = 'main.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = u'Карус'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # I always add this handler to facilitate separating loggings
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(ROOT, '../../log/django.log'),
            'maxBytes': '16777216',  # 16megabytes
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'apps': {
            # I keep all my of apps under 'apps' folder, but you can also add them one by one, and this depends on how your virtualenv/paths are set
            'handlers': ['log_file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
    # you can also shortcut 'loggers' and just configure logging for EVERYTHING at once
    'root': {
        'handlers': ['console', 'mail_admins'],
        'level': 'INFO'
    },
}

# custom attrigutes for form elements
INSTALLED_APPS += ('widget_tweaks',)

# mptt
INSTALLED_APPS += ('mptt',)
MPTT_USE_FEINCMS = True

# feincms
INSTALLED_APPS += ('feincms',)

# filebrowser
INSTALLED_APPS = ('filebrowser',) + INSTALLED_APPS
FILEBROWSER_DIRECTORY = 'upload/'
FILEBROWSER_ADMIN_VERSIONS = None

# tinymce
INSTALLED_APPS += ('tinymce',)
TINYMCE_JS_URL = STATIC_URL + 'tiny_mce/tiny_mce.js'
TINYMCE_FILEBROWSER = True
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': '90%',
    'content_css': "/media/css/bootstrap.css, /media/css/corporate.css, /media/css/font-awesome.css",
    'height': '500px',
    'plugins': 'spellchecker,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,'
               'insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,'
               'noneditable,visualchars,nonbreaking,xhtmlxtras,template,lists',
    'theme_advanced_buttons1': 'save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,'
                               'justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect',
    'theme_advanced_buttons2': 'cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,'
                               'blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,'
                               'inserttime,preview,|,forecolor,backcolor',
    'theme_advanced_buttons3': 'tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,'
                               'advhr,|,print,|,ltr,rtl,|,fullscreen',
    'theme_advanced_buttons4': 'insertlayer,moveforward,movebackward,absolute,|,styleprops,spellchecker,|,cite,abbr,'
                               'acronym,del,ins,attribs,|,visualchars,nonbreaking,template,blockquote,pagebreak,|,'
                               'insertfile,insertimage',

    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_toolbar_align': 'left',
    'theme_advanced_statusbar_location': 'bottom',
    'force_br_newlines': 'true',
    'forced_root_block': '',
    'force_p_newlines': 'false',
    'extended_valid_elements': 'iframe[name|src|framespacing|border|frameborder|scrolling|title|height|width],'
                               'object[declare|classid|codebase|data|type|codetype|archive|standby|height|width|'
                               'usemap|name|tabindex|align|border|hspace|vspace]',
}

# константы
INSTALLED_APPS += ('constance',)
CONSTANCE_CONFIG = (
    # ('название переменной', (u'значение по умолчанию', u'название'),'виджет',обязательное?,u'хелп'),
    # ('DEFAULT_TITLE', (u'', u'Заголовок страниц по умолчанию'), 'text', True),
    # ('DEFAULT_KEYWORDS', (u'', u'Keywords по умолчанию'), 'text'),
    # ('DEFAULT_DESCR', (u'', u'Description по умолчанию'), 'text'),
    ('MANAGER_EMAIL', (u'', u'e-mail, на который будут приходить сообщения с формы обратной связи'), 'text', True,
     u'(несколько адресов можно ввести через запятую)'),
    ('EMAIL_FROM', (u'', u'e-mail,с которого будут отправляться сообщения с формы обратной связи'),
     'email', True, u'Обязательное поле'),
    ('ORDER_TO_EMAIL', (
        u'', u'e-mail, на который будут приходить сообщения о заказах (несколько адресов можно ввести через запятую)'),
     'email', True, u'Обязательное поле'),
    ('ORDER_FROM_EMAIL', (
        u'',
        u'e-mail,с которого будут отправляться сообщения с о заказах (несколько адресов можно ввести через запятую)'),
     'email', True, u'Обязательное поле'),
    ('ANNOUNCES_PER_PAGE', (4, u"Акций в списке"), 'int', True, u'настройка пагинации'),
    ('NEWS_PER_PAGE', (4, u"Новостей в списке"), 'int', True, u'настройка пагинации'),
    ('PROGRAM_PER_PAGE', (10, u"Адресов в списке"), 'int', True, u'настройка пагинации'),
    ('ORDER_PER_PAGE', (10, u"Адресов в корзине"), 'int', True, u'настройка пагинации'),

    ('HEAD_FORM', ('', u"Заголовок формы на главной странице"), 'char', False, u''),
    ('MODAL_FORM', ('', u"Заголовок формы связи с менеджером"), 'char', False, u''),
    ('CONTACT_FORM', ('', u"Заголовок формы на странице контакты "), 'char', False, u''),

    ('YA_FEEDBACK', (u'', u"Цель метрики, кнопка 'Обратная связь' "), 'char', False,
     u'идентификатор цели, вводится без ковычек'),
    ('GMAPS_KEY', (u'', u'Ключ API-google'), 'char', False, u'Ключ для использования google maps')
    # ('ABC2', (u'<h3>Заголовок</h3><p>параграф1</p><p>параграф2</p>', u"Тест визивиг"), 'wysiwyg', False, u'неиспользуемое поле для демонстрации ввода визивиг'),
    # ('ABC3', (3.14, u"Тест дробное число"), 'float', False, u'неиспользуемое поле для демонстрации ввода нецелого числа'),
)

# pytils
INSTALLED_APPS += ('pytils',)

# installed apps
INSTALLED_APPS += (
    'main',
    'south',
    'announce',
    'flatpages',
    'simpleseo',
    'simplesitemap',
    'error_manag',
    'news',
    'message',
    'feedback',
    'placeholder',
    'services',
    'slider',
    'mapelements',
    'addressprogram',
    'order',
    'easy_pdf',
)

# Django_compressor (SASS+SCSS support)
INSTALLED_APPS += ('compressor',)

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_OFFLINE_TIMEOUT = 31536000

COMPRESS_OUTPUT_DIR = "compressed"
COMPRESS_URL = MEDIA_URL
COMPRESS_ROOT = MEDIA_ROOT

COMPRESS_DATA_URI_MAX_SIZE = 32000  # 32 KB for IE8 support
COMPRESS_CSS_FILTERS = (
    'compressor.filters.cssmin.CSSMinFilter',
    'compressor.filters.datauri.CssDataUriFilter',
)

COMPRESS_JS_FILTERS = (
    'compressor.filters.jsmin.JSMinFilter',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'sass --compass {infile} {outfile}'),
    ('text/x-scss', 'scss --compass {infile} {outfile}'),
    ('text/coffeescript', '/usr/local/bin/coffee -b --compile --stdio'),
)

STATICFILES_FINDERS += (
    'compressor.finders.CompressorFinder',
)
