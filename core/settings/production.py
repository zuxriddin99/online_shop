from datetime import timedelta
from pathlib import Path
from os import getenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5c^wh6q2o9t!wr(+wm5r@yae)-16f9r*az9(sq%!wzcd%#ls8_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DJANGO_DEBUG", True)
# ALLOWED_HOSTS = ['vikko.uz', 'www.vikko.uz']
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vikkouz_vikko_db',
        'USER': 'vikkouz_vikko_user',
        'PASSWORD': 'B4xgUdY4WZ9GBj4',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            # 'init_command': 'SET default_storage_engine=INNODB',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
    }
}
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'vikkouz_vikko',
#         'USER': 'vikkouz_vikko_user',
#         'PASSWORD': 'B4xgUdY4WZ9GBj4',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
STATIC_ROOT = '/home/vikkouz/public_html/static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets')
]

MEDIA_ROOT = '/home/vikkouz/public_html/media'
MEDIA_URL = "/media/"

from .base import *
