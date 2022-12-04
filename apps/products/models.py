import decimal
from typing import Union

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from pytils.translit import slugify
from constance import config
from django.urls import reverse


class Category(models.Model):
    """Категория товаров"""

    name = models.CharField('Название категории', max_length=100, unique=True)
    slug = models.SlugField('Slug', max_length=105, unique=True, blank=True)
    icon = models.ImageField('Иконка категории', upload_to='images/category/')

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Brand(models.Model):
    """Бренд товаров"""

    name = models.CharField('Название бренда', max_length=100, unique=True)
    slug = models.SlugField('Slug', max_length=105, unique=True, blank=True)
    logo = models.ImageField('Логотип бренда', upload_to='images/brand/', blank=True, null=True)
    description = RichTextUploadingField('Описание бренда', blank=True, null=True)
    seo_keyword = models.CharField(max_length=255)

    class Meta:
        db_table = 'brands'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductPrice(models.Model):
    """Таблица цен товара"""

    product = models.ForeignKey('Product', verbose_name='Товар', on_delete=models.CASCADE, related_name='prices')
    from_quantity = models.PositiveSmallIntegerField('Цена товара от количество', null=True)
    price = models.DecimalField('Цена', decimal_places=0, max_digits=12)
    price_discount = models.DecimalField('Цена со скидкой', decimal_places=0, max_digits=12, blank=True, null=True)

    class Meta:
        db_table = 'products_prices'
        verbose_name = 'Цена товара'
        verbose_name_plural = 'Цены товара'
        ordering = ('-from_quantity',)

    def __str__(self):
        return f'{self.price} начиная от {self.from_quantity}'


class Product(models.Model):
    """Таблица товаров"""

    class PublicationStatus(models.TextChoices):
        """Статус модерации публикации"""

        MODERATION = 'moderation', 'На модерации'
        PUBLISHED = 'published', 'Опубликовано'
        DRAFT = 'draft', 'Черновик'

    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Slug', max_length=205, unique=True, blank=True)
    quantity_in_stock = models.IntegerField('Количество на складе', default=0)
    dosage = models.CharField('Дозировка', max_length=50, blank=True)
    short_desc = models.CharField('Краткое описание товара', max_length=250, blank=True)
    full_desc = RichTextUploadingField('Полное описание товара')
    new = models.BooleanField(default=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name='Бред', on_delete=models.CASCADE, null=True, blank=True)
    publication_status = models.CharField('Статус публикации', choices=PublicationStatus.choices,
                                          default=PublicationStatus.PUBLISHED, max_length=50)
    created_at = models.DateTimeField('Дата и время создания публикации', auto_now=True)
    updated_at = models.DateTimeField('Дата и время создания публикации', auto_now_add=True)
    is_popular = models.BooleanField('Популярный', default=False)
    telegram_link = models.CharField('Ссылка на товар в телеграме', blank=True, null=True, max_length=250)

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.title}')
            self.save(update_fields=('slug',))

    def get_quantity_price(self, quantity=1) -> decimal.Decimal:
        """Возвращает цену за количество"""
        prices = self.prices.all().order_by('from_quantity')
        price = prices.last().price
        for item in prices:  # TODO: Убедиться что сортировка от большого к меньшему
            if quantity >= item.from_quantity:
                price = item.price
        return price

    @property
    def poster(self) -> str:
        if self.images.first():
            return self.images.first().file.url
        return f"/media/{config.PRODUCT_DEFAULT_PHOTO}"

    @property
    def price(self) -> decimal.Decimal:
        return self.prices.last().price

    @property
    def price_discount(self) -> Union[decimal.Decimal, None]:
        return self.prices.last().price_discount

    @property
    def all_prices_with_quantity(self) -> str:
        """Все цены с количеством"""

        result = ''
        for item in self.prices.order_by('from_quantity'):
            result += f'от {item.from_quantity} шт. = $ {item.price}<br>'

        return result

    def get_absolute_url(self):
        return reverse('product-detail',
                       args=[self.slug])


class ProductImage(models.Model):
    """Таблица изображений товаров"""

    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE, related_name='images')
    file = models.ImageField('Изображение', upload_to='images/product/')

    class Meta:
        db_table = 'products_images'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.file.name
