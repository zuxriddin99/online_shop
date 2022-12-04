from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from apps.users.models import UserCartItem, User
from .serializers import UserCartAddSerializer, UserCartSerializer
from rest_framework.exceptions import APIException, NotFound, ValidationError
from rest_framework.response import Response
class UserCartAddView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = UserCartItem.objects.all()
    serializer_class = UserCartAddSerializer

    def post(self, request, *args, **kwargs):

        # tg_user_id = request.headers.get('user_tg_id')
        # user = User.objects.get(tg_user_id=int(tg_user_id))
        user = self.request.user
        print("AA", type(user))

        # FIXME: We have a user phone number so that we should move tg_user_id and add user phone, Siroj
        # print("AAA", user))

        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            raise ValidationError({'detail': 'Invalid data'})

        data = serializer.validated_data
        UserCartItem.objects.create(cart=user.cart, product_id=data['product_id'], quantity=data['product_count'])
        return Response({"msg": "Cart item created"})

class UserCartGetView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserCartSerializer
    queryset = UserCartItem.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cart__user__phone']

    # def get_queryset(self, *args, **kwargs):
    #     user = self.request.user # FIXME, there should be a another user phone
    #     return UserCartItem.objects.filter(cart__user=user)
