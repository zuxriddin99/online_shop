from datetime import timedelta
from pathlib import Path
from os import getenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5c^wh6q2o9t!wr(+wm5r@yae)-16f9r*az9(sq%!wzcd%#ls8_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DJANGO_DEBUG", True)
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.users.context_processors.fet_cart',
                'apps.users.context_processors.footer_categories',
                'apps.users.context_processors.wishlist',

            ],
        },
    },
]

STATIC_URL = 'static/'
# STATIC_ROOT = Path(BASE_DIR).joinpath('static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = (os.getenv('MEDIA_ROOT', os.path.join(BASE_DIR, 'media')))
MEDIA_URL = "/media/"

from .base import *
