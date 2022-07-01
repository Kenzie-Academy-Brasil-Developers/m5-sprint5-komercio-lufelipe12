from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from .mixins import SerializerByMethodMixin
from .permissions import CustomPermission, IsProductOwner


class ProductView(SerializerByMethodMixin, generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomPermission]

    queryset = Product.objects.all()

    serializer_map = {
        "GET": ProductDetailSerializer,
        "POST": ProductSerializer,
    }

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class RetrieveUpdateDestroyAPIView(
    SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView
):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsProductOwner]

    queryset = Product.objects.all()

    serializer_map = {
        "GET": ProductDetailSerializer,
        "PATCH": ProductSerializer,
    }

