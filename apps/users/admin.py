from django.contrib import admin

from apps.users.models import User, UserCart, UserCartItem, Address, Country


class UserCartItemInline(admin.TabularInline):
    model = UserCartItem
    extra = 0
    fields = ('product', 'quantity', 'get_price', 'get_total_amount')
    readonly_fields = ('get_price', 'get_total_amount')

    @staticmethod
    def get_price(obj):
        return obj.price_per_item

    get_price.allow_tags = True
    get_price.short_description = 'Цена за товар'

    @staticmethod
    def get_total_amount(obj):
        return obj.total_amount

    get_total_amount.allow_tags = True
    get_total_amount.short_description = 'Общая сумма товара'


@admin.register(UserCart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    inlines = (UserCartItemInline,)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UserAddressInline(admin.TabularInline):
    model = Address
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone')
    inlines = (UserAddressInline,)


admin.site.register([Address])
