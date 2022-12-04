from rest_framework import serializers
from apps.products.models import Category, ProductPrice, Product, ProductImage, Brand


class CategorySerializer(serializers.ModelSerializer):
    """ Category serializer """

    class Meta:
        fields = '__all__'
        model = Category

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductPrice

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProductImage


class ProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Brand

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    prices = ProductPriceSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = Product