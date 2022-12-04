from apps.users.models import User, UserCart
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    phone = serializers.CharField()
    tg_user_id = serializers.IntegerField()

    # class Meta:
    #     model = User
    #     fields = ['phone', 'tg_user_id']

        # extra_kwargs = {
        #     'phone': {'required': True},
        #     'tg_user_id': {'required': True},
        # }

    def create(self, validated_data):
        phone = validated_data.get('phone')
        tg_user_id = validated_data.get('tg_user_id')

        user, created = User.objects.get_or_create(
            phone=phone
        )
        user.tg_user_id = tg_user_id
        user.save()

        user_cart, cart_created = UserCart.objects.get_or_create(
            user=user
        )

        user.generate_send_message()

        return validated_data
