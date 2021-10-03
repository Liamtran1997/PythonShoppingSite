from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    # Chi co the truy van khi da dang nhap

    # def get_permission(self):
    #     # List thi noi ng co the xem duoc
    #     if self.action == 'list':
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
