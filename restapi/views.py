from django.shortcuts import render

# rest api imports
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from restapi.serializers import ProductSerializer, CategorySerializer, ProductBrandSerializer
from apps.products.models import Product, Category, Brand


class CategoryListView(generics.ListAPIView):
    """ Category list view """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)


class BrandListView(generics.ListAPIView):
    """ Brands list view """
    queryset = Brand.objects.all()
    serializer_class = ProductBrandSerializer
    permission_classes = (IsAuthenticated,)

class ProductListView(generics.ListAPIView):
    """ Product List view """
    queryset = Product.objects.prefetch_related('prices', 'images')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'brand']
    permission_classes = (IsAuthenticated,)

class ProductDetailView(generics.RetrieveAPIView):
    """ Product detail view """
    queryset = Product.objects.prefetch_related('prices', 'images')
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)


