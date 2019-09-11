from rest_framework import serializers

from core.models import Product
from core.models import WishList
from core.models import UserMagalu


class UserMagaluSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserMagalu

        fields = [
            'id',
            'username',
            'email',
        ]

        read_only_fields = ['id']

        required = ['username', 'email']


class UserMagaluSerializerReadOnly(serializers.ModelSerializer):

    class Meta:
        model = UserMagalu

        fields = [
            'id',
            'username',
        ]


class WishListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WishList

        fields = '__all__'

        read_only_fields = ['magalu_user']

        required = ['magalu_user']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        fields = '__all__'

        required = ['product_id', 'wishlist']
