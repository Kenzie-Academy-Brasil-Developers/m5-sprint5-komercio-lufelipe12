from asyncore import read
from attr import field
from rest_framework import serializers

from .models import Product
from users.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):
    seller = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "description",
            "price",
            "quantity",
            "is_active",
            "seller",
        ]
        extra_kwargs = {
            "is_active": {"default": True},
            "quantity": {"min_value": 0},
        }


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "description",
            "price",
            "quantity",
            "is_active",
            "seller_id",
        ]
        extra_kwargs = {
            "is_active": {"default": True},
            "seller_id": {"read_only": True},
        }
