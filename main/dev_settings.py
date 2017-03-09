from settings import *

DEBUG = True

COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/email-messages/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'karus',
        'USER': 'root',
        'PASSWORD': '111111',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}