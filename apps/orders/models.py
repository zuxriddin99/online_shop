from django.conf import settings
from django.db import models

from apps.products.models import Product
from apps.users.models import UserCartItem, Address


class OrderStatus(models.Model):
    name = models.CharField(verbose_name='Название статуса заказа', max_length=100)

    class Meta:
        db_table = 'order_status'
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return self.name


class Order(models.Model):
    """Таблица заказов"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Клиент', on_delete=models.CASCADE,
                             related_name='orders')
    total_cost = models.DecimalField('Сумма заказа', decimal_places=0, max_digits=12)
    paid = models.BooleanField('Оплачено', default=False)
    status = models.ForeignKey(OrderStatus, on_delete=models.RESTRICT, verbose_name='Статус заказа', null=True)
    created_at = models.DateTimeField('Дата и время заказа', auto_now=True)
    update_at = models.DateTimeField('Дата и время изменения заказа', auto_now_add=True)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True, verbose_name='Адрес')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'№ {self.id + settings.ORDER_NUMBER}'


class OrderItem(models.Model):
    """Таблица товаров заказа"""

    order = models.ForeignKey(Order, verbose_name='Заказ', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.SET_NULL, null=True,
                                related_name='orders')
    product_title = models.CharField('Название товара', max_length=100, blank=True)
    product_image = models.CharField('Изображение товара', max_length=250, blank=True)
    product_price = models.DecimalField('Цена товара', decimal_places=0, max_digits=12, blank=True)
    product_quantity = models.IntegerField('Количество', default=1)
    product_total_amount = models.DecimalField('Общая сумма за товар', decimal_places=0, max_digits=12)

    class Meta:
        db_table = 'orders_items'
        verbose_name = 'Товар заказа'
        verbose_name_plural = 'Товары заказа'

    def __str__(self):
        return self.product_title

    def save_product_info(self, cart_item: UserCartItem):
        """Сохранение доп. информации товара"""

        self.product_title = cart_item.product.title
        self.product_image = cart_item.product.images.first().file.url
        self.product_price = cart_item.price_per_item
        self.product_quantity = cart_item.quantity
        self.product_total_amount = cart_item.total_amount
        self.save(update_fields=('product_title', 'product_image', 'product_price', 'product_quantity',
                                 'product_total_amount'))
