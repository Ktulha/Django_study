from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import ProductSerializer, UserSerializer, WarehouseSerializer
from api.models import ApiUser, Product, Warehouse


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post', 'get']


class WarehouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
