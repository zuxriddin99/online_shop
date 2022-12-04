from django.contrib import admin

from apps.products.models import Category, Brand, Product, ProductImage, ProductPrice


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductPriceInline(admin.TabularInline):
    model = ProductPrice
    extra = 5


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    inlines = (ProductPriceInline, ProductImageInline)


admin.site.register([Category, Brand])
