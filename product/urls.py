from django.contrib import admin
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('product', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list-category/', views.listcategory, name='list-category'),
    path('list-product//', views.listproduct, name='list-product'),
    path('create-category/', views.createcategory, name='create-category'),
]
