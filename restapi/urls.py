from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny

from apps.users.models import User
from .cart.serializers import UserCartAddSerializer
from .cart.views import UserCartAddView, UserCartGetView
from .views import ProductListView, CategoryListView, BrandListView, ProductDetailView
from restapi.user.views import UserCreateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Vikko API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@vikko.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[AllowAny],
)

#jwt auth
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
   path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('docs/category/', CategoryListView.as_view(), name='category-api'),
   path('docs/brands/', BrandListView.as_view(), name='brand-api'),
   path('docs/product/', ProductListView.as_view(), name='product-api'),
   path('docs/product/<pk>', ProductDetailView.as_view(), name='detail-product'),
   # Cart urls
   path('docs/cart/create/', UserCartAddView.as_view(), name="add-to-cart"),
   path('docs/cart/get/', UserCartGetView.as_view(), name="get-cart-items"),
   # User urls
   path('docs/user/post/', UserCreateView.as_view(), name="user-create"),
   # path('docs/auth/', CustomAuthToken.as_view()),

   #jwt token
   path('api/user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
