from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.response import Response
# Create your views here.

# Hiển thị danh sách Category
@api_view(['GET'])
def listcategory(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def listproduct(request):
    product = Product.objects.all()
    serializer = CategorySerializer(product, many=True)
    return Response(serializer.data)

# Hiển thị form tạo mới 1 Category
@api_view(['POST'])
def createcategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]
    # Chi co the truy van khi da dang nhap


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]


