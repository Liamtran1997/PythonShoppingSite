from django.contrib import admin
from . import views
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('product', views.CategoryViewSet)
router.register('product', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
