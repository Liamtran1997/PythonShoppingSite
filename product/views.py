from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.response import Response
# from . services import
# Create your views here.


# Hiển thị danh sách Category
@api_view(['GET'])
def list_category(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_product(request):
    product = Product.objects.all()
    serializer = CategorySerializer(product, many=True)
    return Response(serializer.data)


# Hiển thị form tạo mới 1 Category
@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    try:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    except:
        return HttpResponse("Something went wrong!!!")


@api_view(['POST'])
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(data=request.data)
    try:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
    except:
        return HttpResponse("Something went wrong!!!")


@api_view(['DELETE'])
def deleted_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response("This Category successfully delete!")


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]
    # Chi co the truy van khi da dang nhap


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]







