import datetime
from random import choice
from string import digits

import requests
from constance import config
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.core import serializers
from django.db.models import Q, Count
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from apps.main.models import Settings

from apps.products.models import Product, Category, ProductPrice, Brand, ProductImage
from apps.users.cart import Cart
from apps.orders.models import Order, OrderStatus, OrderItem
from apps.users.models import UserCartItem, User, UserCart, UserForm, UserSMSCode, Country, Address
from apps.users.forms import AddressForm
from django.contrib.auth import login as django_login

from core.sms_service import sms_to_phone


class ShopView(ListView):
    """Шаблон магазина"""

    template_name = 'shop/index.html'
    model = Product
    paginate_by = 12
    context_object_name = 'products'

    # queryset = Product.objects.filter(publication_status='published')

    def get_context_data(self, *args, **kwargs):
        first = ProductPrice.objects.order_by('price').first()
        last = ProductPrice.objects.order_by('-price').first()
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all().order_by('name')
        context['category_name'] = 'Каталог'
        context['config'] = config
        context['product_price_min'] = first.price if first else 1
        context['product_price_max'] = last.price if last else 500
        return context

    # FIXME: баг с пагинацией из за фильтрации товаров по категориям таким способом
    def get_queryset(self):
        user = self.request.user
        category_id = self.request.GET.get('category') if 'category' in self.request.GET else None
        brand_id = self.request.GET.get('brand') if 'brand' in self.request.GET else None
        search_text = self.request.GET.get('search') if 'search' in self.request.GET else None
        min_price = self.request.GET.get('min_price') if 'min_price' in self.request.GET else None
        max_price = self.request.GET.get('max_price') if 'max_price' in self.request.GET else None
        filters = Q(publication_status='published')
        if category_id:
            filters = filters & Q(category_id=category_id)
            # return Product.objects.filter(category_id=category_id, publication_status='published')
        if brand_id:
            filters = filters & Q(brand_id=brand_id)
            # return Product.objects.filter(category_id=category_id, publication_status='published')
        if search_text:
            filters = filters & Q(title__icontains=search_text)
            # return Product.objects.filter(title__icontains=search_text, publication_status='published')
        if min_price and max_price:
            # return Product.objects.filter(publication_status='published')
            p = list(ProductPrice.objects.filter(
                Q(product__publication_status='published') & Q(price__lte=max_price) & Q(
                    price__gte=min_price)).values_list('product_id', flat=True))
            filters = filters & Q(id__in=p)
            # return Product.objects.prefetch_related('favorites_users').filter(id__in=p).annotate(
            #     is_favourite=favourites_user)
        if user.is_anonymous:
            resp = Product.objects.filter(filters)
        else:
            resp = Product.objects.filter(filters).prefetch_related('favorites_users').annotate(
                is_favourite=Count('favorites_users', filter=Q(favorites_users=user)))

        return resp


class BrandView(ListView):
    template_name = 'brand/brand.html'
    model = Product
    paginate_by = 5
    context_object_name = 'products'

    # queryset = Product.objects.filter(publication_status='published')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['brand'] = Brand.objects.get(slug=self.kwargs.get('slug'))
        # context['config'] = config
        return context

    # FIXME: баг с пагинацией из за фильтрации товаров по категориям таким способом
    def get_queryset(self):
        user = self.request.user
        brand_slug = self.kwargs.get('slug')
        filters = Q(publication_status='published', brand__slug=brand_slug)
        if user.is_anonymous:
            resp = Product.objects.filter(filters)
        else:
            resp = Product.objects.filter(filters).prefetch_related('favorites_users').annotate(
                is_favourite=Count('favorites_users', filter=Q(favorites_users=user)))
        return resp


class ProductDetailView(DetailView):
    """Карточка товара"""

    template_name = 'products/index.html'
    model = Product
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = Product.objects.filter(category=self.object.category).exclude(id=self.object.id)
        return context


def add_cart(request):
    """Добавление товара в корзину"""

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity', 1)
        product = get_object_or_404(Product, id=product_id)
        cart = Cart(request)
        cart.add(product, quantity)
        print(request.POST.get('redirect_url'))
        return redirect(f"{request.POST.get('redirect_url')}")


def remove_cart(request):
    """Удалениа товара от корзину"""

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart = Cart(request)
        cart.remove(product)
        return redirect(f"{request.POST.get('redirect_url')}")


def decrement_item_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        cart = Cart(request)
        cart.decrement(product)
        return redirect(f"{request.POST.get('redirect_url')}")


def cart_detail(request):
    """Страница корзины"""

    cart = Cart(request)
    a = False if len([i for i in cart]) else True
    if request.user.is_authenticated:
        adr = request.user.addresses.all()
        have_adr = True if adr else False
        return render(request,
                      template_name='cart/index.html',
                      context={
                          'cart': cart,
                          'adr': adr,
                          'have_adr': have_adr,
                          'countries': Country.objects.all(),
                          'cart_empty': a
                      })
    else:
        return render(request, template_name='cart/index.html', context={'cart': cart, 'cart_empty': a})


def is_ajax(request) -> bool:
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def get_random_code(length=6) -> str:
    return ''.join([choice(digits) for _ in range(length)])


def send_sms_code(user: User) -> int:
    # code = get_random_code() # todo
    code = 123456
    # sms_to_phone(user.phone, f"Code - {code}")
    return int(code)


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        return render(request, template_name='login/index.html', context={})

    if request.method == 'POST' and is_ajax(request):
        data = request.POST
        phone = data.get('phone')
        sms_code = data.get('sms_code')

        user, _ = User.objects.get_or_create(phone=str(phone), username=str(phone))
        if not sms_code:
            code = send_sms_code(user)
            UserSMSCode.objects.create(user=user, code=code)
            return JsonResponse({'success': True, 'message': 'Смс отправлен на указанный номер', 'redirect': False},
                                status=200)
        user_sms_code = user.codes.last()
        TIMEOUT = 1
        # if user_sms_code.created_at + datetime.timedelta(hours=TIMEOUT) < datetime.datetime.now():
        #     JsonResponse({'success': False, 'message': 'Срок смс-кода истёк'}, status=400)
        if str(user_sms_code.code) != str(sms_code):
            return JsonResponse({'success': False, 'message': 'Неверный код'}, status=400)
        django_login(request, user)
        return JsonResponse({'success': True, 'redirect': True, 'message': 'Вы успешно авторизовались'}, status=200)


from django.contrib.auth.models import AnonymousUser


@login_required(login_url='/login/')
def add_favourite(request):
    if request.method == 'POST':
        user = request.user
        product = get_object_or_404(Product, id=request.POST.get('product_id'))
        user.favorites.add(product)
        return redirect(f"{request.POST.get('redirect_url')}")


@login_required(login_url='/login/')
def remove_favourite(request):
    if request.method == 'POST':
        user = request.user
        product = get_object_or_404(Product, id=request.POST.get('product_id'))
        user.favorites.remove(product)
        return redirect(f"{request.POST.get('redirect_url')}")
