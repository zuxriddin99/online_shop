from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, DeleteView

from apps.orders.models import OrderStatus, Order
from apps.products.models import ProductPrice
from apps.users.forms import AddressForm
from apps.users.models import User, Country, Address
from django.contrib.auth import logout as django_logout


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileView(DetailView):
    template_name = 'profile/index.html'
    model = User
    context_object_name = 'user_data'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_statuses'] = OrderStatus.objects.all()
        context['all_orders'] = 'Все заказы'
        context['orders'] = self.order_status_filter()
        context['addresses'] = self.request.user.addresses.all().order_by('-default')
        context['countries'] = Country.objects.all()
        context['product_price_max'] = ProductPrice.objects.order_by('-price').first().price
        return context

    def order_status_filter(self):
        if self.request.GET.get('status', 0):
            return Order.objects.filter(user=self.request.user, status_id=self.request.GET.get('status', int))
        else:
            return Order.objects.filter(user=self.request.user)


class AddAddress(CreateView):
    model = Address

    def post(self, request, *args, **kwargs):
        form = AddressForm(request.POST)
        adr = form.save()
        adr.save()
        return HttpResponseRedirect('/profile/')


def logout_user(request):
    django_logout(request)
    return HttpResponseRedirect('/shop/')


class DeleteAddress(DeleteView):
    model = Address
