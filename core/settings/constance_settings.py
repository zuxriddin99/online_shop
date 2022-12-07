from decimal import Decimal

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_REDIS_CACHE_TIMEOUT = 60
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True
CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {}]
}

CONSTANCE_CONFIG = {
    'CURRENCY': (Decimal(110000), 'один доллар в сумме', Decimal),

    'SEO_HOME_TITLE': ('title', 'Заголовок гл. страницы'),
    'SEO_HOME_KEYWORDS': ('keywords', 'Кейвордс гл. страницы'),
    'SEO_HOME_DESC': ('desc', 'Описание гл. страницы'),
    'SEO_HOME_URL': ('https://vikko.uz/', 'Адрес сайта'),
    'SEO_HOME_IMAGE': ('images/master-slide-03.jpg', 'Описание гл. страницы', 'image_field'),

    'SEO_SHOP_TITLE': ('title', 'Заголовок магазин страницы'),
    'SEO_SHOP_KEYWORDS': ('keyword', 'Кейвордс магазин страницы'),
    'SEO_SHOP_DESC': ('dedsc', 'Описание магазин страницы'),
    'SEO_SHOP_URL': ('https://vikko.uz/', 'Адрес сайта'),
    'SEO_SHOP_IMAGE': ('images/master-slide-03.jpg', 'Описание магазин страницы', 'image_field'),

    'SEO_PRODUCTS_TITLE': ('title', 'Заголовок продукт страницы'),
    'SEO_PRODUCTS_KEYWORDS': ('keyword', 'Кейвордс продукт страницы'),
    'SEO_PRODUCTS_DESC': ('desc', 'Описание продукт страницы'),
    'SEO_PRODUCTS_URL': ('https://vikko.uz/', 'Адрес сайта'),
    'SEO_PRODUCTS_IMAGE': ('images/master-slide-03.jpg', 'Описание продукт страницы', 'image_field'),

    'SEO_BLOG_TITLE': ('title', 'Заголовок гл. страницы'),

    'S1': ('images/master-slide-03.jpg', 'Изображение в слайдере \n Рекомендуемый размер изображения 1920x570!',
           'image_field'),
    'S1_TITLE1': ('Women Collection 2018', 'Не жирный заголовок в слайдере'),
    'S1_TITLE2': ('Women Collection 2018', 'Жирный заголовок в слайдере'),
    'S2': ('images/master-slide-03.jpg', 'Изображение в слайдере\nРекомендуемый размер изображения 1920x570!',
           'image_field'),
    'S2_TITLE1': ('Women Collection 2018', 'Не жирный заголовок в слайдере'),
    'S2_TITLE2': ('Women Collection 2018', 'Жирный заголовок в слайдере'),
    'S3': ('images/master-slide-03.jpg', 'Изображение в слайдере\nРекомендуемый размер изображения 1920x570!',
           'image_field'),
    'S3_TITLE1': ('Women Collection 2018', 'Не жирный заголовок в слайдере'),
    'S3_TITLE2': ('Women Collection 2018', 'Жирный заголовок в слайдере'),
    'B1': ('images/banner-02.jpg',
           'Первое изображение баннера на главной странице \n Рекомендуемый размер изображения 720x932!',
           'image_field'),
    'B1_CAT_ID': (1, 'ИД категории первого баннера'),
    'B2': ('images/banner-05.jpg',
           'Второй изображение баннера на главной странице \n Рекомендуемый размер изображения 720x660!',
           'image_field'),
    'B2_CAT_ID': (1, 'ИД категории второго баннера'),
    'B3': ('images/banner-02.jpg',
           'Третье изображение баннера на главной странице \n Рекомендуемый размер изображения 720x932!',
           'image_field'),
    'B3_CAT_ID': (1, 'ИД категории третьего баннера'),

    'B4': ('images/banner-05.jpg',
           'Четвертое изображение баннера на главной странице \n Рекомендуемый размер изображения 720x660!',
           'image_field'),
    'B4_CAT_ID': (1, 'ИД категории четвертого баннера'),

    'B5': ('images/banner-02.jpg',
           'Пятое изображение баннера на главной странице \n Рекомендуемый размер изображения 720x932!',
           'image_field'),
    'B5_CAT_ID': (1, 'ИД категории пятого баннера'),
    'B6': ('images/banner-05.jpg',
           'Седьмое изображение баннера на главной странице \n Рекомендуемый размер изображения 720x660!',
           'image_field'),
    'B6_CAT_ID': (1, 'ИД категории пятого баннера'),
    'PRODUCT_DEFAULT_PHOTO': ('images/master-slide-03.jpg', 'Фото товара по умолчанию',
                              'image_field'),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Валюта': {
        'fields': ('CURRENCY',),
        'collapse': True
    },
    'Настройки SEO': {
        'fields': ('SEO_HOME_TITLE', 'SEO_HOME_KEYWORDS', 'SEO_HOME_DESC', 'SEO_HOME_URL', 'SEO_HOME_IMAGE'),
        'collapse': True
    },
    'Настройки Продукт SEO': {
        'fields': ('SEO_PRODUCTS_TITLE', 'SEO_PRODUCTS_KEYWORDS', 'SEO_PRODUCTS_DESC', 'SEO_PRODUCTS_URL', 'SEO_PRODUCTS_IMAGE'),
        'collapse': True
    },
    'Настройки Магазин SEO': {
        'fields': ('SEO_SHOP_TITLE', 'SEO_SHOP_KEYWORDS', 'SEO_SHOP_DESC', 'SEO_SHOP_URL', 'SEO_SHOP_IMAGE'),
        'collapse': True
    },
    'Настройки Блог SEO': {
        'fields': ('SEO_BLOG_TITLE', ),
        'collapse': True
    },
    'Фото': {
        'fields': ('PRODUCT_DEFAULT_PHOTO',),
        'collapse': True
    },
    'Первый слайдер': {
        'fields': ('S1', 'S1_TITLE1', 'S1_TITLE2'),
        'collapse': True
    },
    'Второй слайдер': {
        'fields': ('S2', 'S2_TITLE1', 'S2_TITLE2'),
        'collapse': True
    },
    'Третий слайдер': {
        'fields': ('S3', 'S3_TITLE1', 'S3_TITLE2'),
        'collapse': True
    },
    'Баннер категории': {
        'fields': ('B1', 'B1_CAT_ID', 'B2', 'B2_CAT_ID', 'B3', 'B3_CAT_ID', 'B4', 'B4_CAT_ID', 'B5', 'B5_CAT_ID', 'B6',
                   'B6_CAT_ID'),
        'collapse': True
    }
}
