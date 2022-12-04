from requests import Response
from rest_framework import serializers

from apps.products.models import Product
from apps.users.models import User, UserCart, UserCartItem


class UserCartAddSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)
    product_count = serializers.IntegerField(default=0)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone']

class ProductCartSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'category']
        model = Product

class CartUserPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['phone', 'tg_user_id']
        model = User

class CartUsersSerializer(serializers.ModelSerializer):
    user = CartUserPhoneSerializer()
    class Meta:
        fields = ['user']
        model = UserCart

class UserCartSerializer(serializers.ModelSerializer):
    product = ProductCartSerializer()
    cart = CartUsersSerializer()
    class Meta:
        model = UserCartItem
        fields = ['cart', 'product', 'quantity']
