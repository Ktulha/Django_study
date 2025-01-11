from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

from api.serializers import ProductSerializer, StockSerializer, TransactionSerializer, TransactionViewSerializer, UserSerializer, WarehouseSerializer
from api.models import ApiUser, Product, Stock, Transaction, Warehouse


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = ApiUser .objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post']
    permission_classes = [permissions.AllowAny]


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['post', 'get']
    permission_classes = [permissions.IsAuthenticated]


class WarehouseModelViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionCreateView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()

    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransactionViewSerializer
        elif self.request.method == 'POST':
            return TransactionSerializer
        return ProductSerializer

    def perform_create(self, serializer):
        try:
            user = self.request.user
            serializer.save(user=user)
        except ValidationError as e:
            return Response({"error": str(e)}, status=400)


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get']
