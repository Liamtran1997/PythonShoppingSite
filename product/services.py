from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status


# class CategoryServices:
def list_category_services():

    try:
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    except:
        return Response(status=status.HTTP_200_OK)


def list_product_services():

    try:
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    except:
        return Response(status=status.HTTP_200_OK)


def create_category_services(request):

    serializer = CategorySerializer(data=request.data)

    try:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    except:
        return Response(status=status.HTTP_200_OK)


def update_category_services(request, pk):

    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)

    try:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    except:
        return Response(status=status.HTTP_200_OK)


def delete_category_services(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response(status=status.HTTP_200_OK)






