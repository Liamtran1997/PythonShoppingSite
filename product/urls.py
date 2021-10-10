from django.contrib import admin
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('product', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list-category/', views.list_category, name='list-category'),
    path('list-product/', views.list_product, name='list-product'),
    path('create-category/', views.create_category, name='create-category'),
    path('update-category/<str:pk>/', views.update_category, name='update-category'),
    path('delete-category/<str:pk>/', views.deleted_category, name='delete-category'),
]


