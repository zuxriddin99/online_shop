import decimal

from django.conf import settings
from django.core import serializers

from apps.products.models import Product


class Cart:
    """Корзина пользователя"""

    def __init__(self, request):
        """Инициализация корзины"""

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if cart is None:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product: Product, quantity=1, update_quantity: bool = False):
        """Добавление товара в корзину"""

        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                # 'product': serializers.serialize('json', [product]),
                'quantity': quantity
            }
        else:
            if update_quantity:
                self.cart[product_id]['quantity'] = quantity
            else:
                self.cart[product_id]['quantity'] = int(self.cart[product_id]['quantity']) + int(quantity)

        self.save()

    def save(self):
        """Обновление корзины"""

        self.session[settings.CART_SESSION_ID] = self.cart
        # Пометить сеанс как «измененный», чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product: Product):
        """Удаление товара из корзины."""

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product: Product):
        """Уменьшение количество"""

        product_id = str(product.id)
        if product_id in self.cart:
            if int(self.cart[product_id]['quantity']) > 1:
                self.cart[product_id]['quantity'] = int(self.cart[product_id]['quantity']) - 1
                self.save()
            else:
                return self.remove(product)

    def clear(self):
        """Очистка корзины"""

        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    @property
    def total_cost(self):
        """Подсчет стоимости товаров в корзине."""

        return sum(decimal.Decimal(item['total_amount']) for item in self.cart.values())

    @staticmethod
    def price_per_item(product: Product, quantity) -> decimal.Decimal:
        """Возвращает цену за товар со скидкой в зависимости от количества."""
        return product.get_quantity_price(quantity=quantity)

    @staticmethod
    def total_amount(price_per_item: decimal.Decimal, quantity: int) -> decimal.Decimal:
        """Возвращает итоговую сумму за 1 товар"""
        return price_per_item * quantity

    def __iter__(self):
        """Перебор элементов в корзине и получение продуктов из базы данных."""

        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product
        deleted_keys = []

        for item in self.cart.values():
            quantity = int(item['quantity'])
            price_per_item = self.price_per_item(item['product'], quantity)
            total_amount = self.total_amount(price_per_item, quantity)
            item['price'] = price_per_item
            item['total_amount'] = total_amount
            yield item

    @property
    def get_count_items(self) -> int:
        """Возвращает количество товаров в корзине"""
        self.products_checker_from_db()
        return len(self.cart)

    def products_checker_from_db(self):
        cart_values = list(int(i) for i in self.cart.keys())
        products = Product.objects.filter(id__in=cart_values).only('id').values_list('id', flat=True)
        unique_items = list(set(cart_values).symmetric_difference(set(products)))
        if unique_items:
            for i in unique_items:
                del self.cart[str(i)]
