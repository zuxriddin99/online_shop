from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import apps.main.views
from apps.main.views import HomePage, wholesaler_page, BlogDetail, BlogPage, AboutUsDetail
from apps.products.sitemaps import ProductSitemap
from apps.products.views import ShopView, ProductDetailView, add_cart, login, cart_detail, remove_cart, \
    decrement_item_cart, add_favourite, remove_favourite, BrandView
from apps.users.views import ProfileView, AddAddress, logout_user, DeleteAddress
from apps.orders.views import CreateOrder, OrderDetailView
from django.contrib.flatpages import views
from django.contrib.sitemaps.views import sitemap, index

handler404 = 'apps.main.views.handler404'


sitemaps = {
    'products': ProductSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', HomePage.as_view(), name='home-page'),
    path('blog/<int:id>/', BlogDetail.as_view(), name='blog-detail'),
    path('blog/blog-list/', BlogPage.as_view(), name='blog-page'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<str:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('brand/<str:slug>/', BrandView.as_view(), name='brand'),
    path('add-favourite/', add_favourite, name='add-favourite'),
    path('remove-favourite/', remove_favourite, name='remove-favourite'),
    path('address/<int:pk>/delete/', DeleteAddress.as_view(), name='delete-address'),
    path('add-cart/', add_cart, name='add-cart'),
    path('remove-cart/', remove_cart, name='remove-cart'),
    path('decrement-item-cart/', decrement_item_cart, name='decrement-item-cart'),
    path('cart/', cart_detail, name='cart'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('about-us/', AboutUsDetail.as_view(), name='about-us'),
    path('add/address/', AddAddress.as_view(), name='add-address'),
    path('create/order/', CreateOrder.as_view(), name='create-order'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('wholesaler/', wholesaler_page, name='wholesaler-form'),
    # path('i18n/', include('django.conf.urls.i18n')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('delivery/', views.flatpage, {'url': '/delivery/'}, name='delivery'),
    path('payment-return/', views.flatpage, {'url': '/payment-return/'}, name='payment-return'),
    path('v1/', include('restapi.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),


]
# urlpatterns += i18n_patterns(
#
# )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
