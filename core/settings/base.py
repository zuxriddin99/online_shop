import os
from datetime import timedelta
from pathlib import Path

from .locale import SECRET_KEY

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

INTERNAL_IPS = [
    'localhost',
    "127.0.0.1",
]

PROJECT_LIBS = [
    'debug_toolbar',
    'ckeditor',
    'ckeditor_uploader',
    'constance',
    'constance.backends.database',
    'django_cron',
    'rest_framework',
    'drf_yasg',
    'django_filters',
    # 'rest_framework.authtoken',
    'rest_framework_simplejwt',

]
PROJECT_APPS = [
    'apps.main',
    'apps.users',
    'apps.products',
    'apps.orders',
]

INSTALLED_APPS = [
                     # 'modeltranslation',
                     'django.contrib.admin',
                     'django.contrib.auth',
                     'django.contrib.contenttypes',
                     'django.contrib.sessions',
                     'django.contrib.messages',
                     'django.contrib.staticfiles',
                     'django.contrib.sites',
                     'django.contrib.sitemaps',
                     'django.contrib.flatpages',

                 ] + PROJECT_LIBS + PROJECT_APPS

SITE_ID = 1

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES':
        ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,

}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=90),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=90),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),

}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
]

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

# gettext = lambda s: s
#
# LANGUAGES = (
#     ('ru', gettext('Russia')),
#     ('uz', gettext('Uzbek')),
# )

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'users.User'

ORDER_NUMBER = 1500

CART_SESSION_ID = 'cart'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRON_CLASSES = [
    "core.cron.MyCronJob",
    # ...
]
SITE_ID = 1
from .ckeditor_config import *
from .constance_settings import *
