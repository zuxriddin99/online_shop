import logging
from decimal import Decimal

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView

from apps.orders.models import OrderStatus, Order, OrderItem
from apps.products.models import ProductPrice, Product
from apps.users.cart import Cart
from apps.users.models import User, Country, Address
from django.contrib import messages

from core.sms_service import sms_to_phone


class CreateOrder(CreateView):
    model = Order

    def post(self, request, *args, **kwargs):
        data = request.POST
        try:
            address_from = int(data.get('address_from'))
        except Exception as error:
            address_from = False
        if bool(address_from):
            address_id = address_from
        elif data.get('country') and data.get('city') and data.get('address'):
            logging.error(data.get('country'))

            address_id = Address.objects.create(user=self.request.user, country_id=data.get('country'),
                                                city=data.get('city'),
                                                address=data.get('address')).id
            logging.error(address_id)

        else:
            messages.error(self.request, 'Вы должны ввести адрес', extra_tags='danger')
            return HttpResponseRedirect('/cart/')
        order = self.create_order(request, address_id)
        messages.success(self.request, 'Заказ успешно создан.')
        # sms_to_phone(message=f"New order create №{order.id}")
        return HttpResponseRedirect('/cart/')

    def create_order(self, request, address):
        cart = Cart(request)
        order = Order.objects.create(user=self.request.user, status_id=1, total_cost=0, address_id=address)
        total_cost = Decimal(0)
        for prod in cart:
            product: Product = prod.get('product')
            quantity = int(prod.get('quantity'))
            price = product.get_quantity_price(quantity)
            prod_total_price = price * Decimal(quantity)
            OrderItem.objects.create(order=order, product=product,
                                     product_title=prod.get('product').title,
                                     product_price=price,
                                     product_quantity=quantity,
                                     product_total_amount=prod_total_price)
            total_cost += prod_total_price
        cart.clear()
        order.total_cost = total_cost
        order.save(update_fields=('total_cost',))
        return order

class OrderDetailView(DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.items.all()
        return context
