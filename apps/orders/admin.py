from urllib.parse import urlencode

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from apps.orders.models import *


# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_cost', 'paid', 'created_at')
    inlines = (OrderItemInline,)
    list_filter = ('status', 'paid')
    search_fields = ('users',)

    # def view_students_link(self, obj):
    #     url = (
    #             reverse("admin:users")
    #             + "?"
    #             + urlencode({"courses__id": f"{obj.id}"})
    #     )
    #     return format_html('<a href="{}">{} Students</a>', url)
    #
    # view_students_link.short_description = "Students"


@admin.register(OrderItem)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
