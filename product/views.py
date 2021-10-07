from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.response import Response
from . services import list_category_services, list_product_services, \
    create_category_services, delete_category_services, update_category_services
# Create your views here.


# Hiển thị danh sách Category
@api_view(['GET'])
def list_category(request):
    return list_category_services()


@api_view(['GET'])
def list_product(request):
    return list_product_services()


@api_view(['POST'])
def create_category(request):
    return create_category_services(request)


@api_view(['PUT'])
def update_category(request, pk):
    update_category_services(request, pk)


@api_view(['DELETE'])
def deleted_category(request, pk):
    delete_category_services(request, pk)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]
    # Chi co the truy van khi da dang nhap


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]







