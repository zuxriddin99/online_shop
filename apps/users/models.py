import decimal

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

from apps.products.models import Product


class UserManager(BaseUserManager):
    """Менеджер для переопределения методов авторизации/регистрации"""

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(phone, password, **extra_fields)


class User(AbstractUser):
    """Модель юзеров"""

    phone = models.CharField('Номер телефона', max_length=15, unique=True,
                             help_text='Без +')  # Авторизация по номеру телефона

    objects = UserManager()
    favorites = models.ManyToManyField(Product, verbose_name='Избранное продукты', related_name='favorites_users')
    USERNAME_FIELD = "phone"
    # REQUIRED_FIELDS = ["username"]
    tg_user_id = models.IntegerField(blank=True, null=True)
    username = models.CharField(blank=True, null=True, max_length=250)

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.id)

    def generate_send_message(self):
        import random
        from .utils import send_message

        # number = random.randint(100000, 999999) # TODO: Sms code integration, utils
        number = '123456'
        send_message(self.phone, number)
        self.set_password(number)
        self.save()


class Country(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'countries'
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self.name


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='addresses')
    city = models.CharField(max_length=150, null=True)
    address = models.CharField(verbose_name='Адрес', default='', max_length=300)
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.PROTECT, null=True)
    default = models.BooleanField(default=False)

    class Meta:
        db_table = 'addresses'
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.address


class UserSMSCode(models.Model):
    """Таблица с кодами пользователя"""

    user = models.ForeignKey(User, verbose_name='Пользователь', related_name='codes', on_delete=models.CASCADE)
    code = models.IntegerField('Код из смс', blank=True, null=True)
    created_at = models.DateTimeField('Дата и время отправленного смс', auto_now=True)

    class Meta:
        db_table = 'users_codes'
        verbose_name = 'Код из смс'
        verbose_name_plural = 'Коды из смс-ок'

    def __str__(self):
        return f'{self.code}'


class UserForm(forms.Form):
    """Форма для регистрации/авторизации"""

    phone = models.BigIntegerField('Номер телефона', help_text='Ввод без +')
    sms_code = models.CharField('СМС-код', blank=True, help_text='Введите код из смс')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        ## add a "form-control" class to each form input

        ## for enabling bootstrap

        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({

                'class': 'form-control',

            })


class UserCart(models.Model):
    """ Корзина пользователя"""

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='cart')

    class Meta:
        db_table = 'users_carts'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return str(self.user.username)

    @property
    def total_cost(self):
        return sum([item.total_amount for item in self.items.all()])


class UserCartItem(models.Model):
    """ Товары в корзине пользователя """

    cart = models.ForeignKey(UserCart, verbose_name='Корзина', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField('Количество', default=1)

    class Meta:
        db_table = 'users_carts_items'
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return self.product.title

    @property
    def price_per_item(self) -> decimal.Decimal:
        """Возвращает цену за товар со скидкой в зависимости от количества."""

        return self.product.get_quantity_price(quantity=self.quantity)

    @property
    def total_amount(self) -> decimal.Decimal:
        """Возвращает итоговую сумму за 1 товар"""

        return self.price_per_item * self.quantity
