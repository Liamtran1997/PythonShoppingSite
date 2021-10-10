from django.urls import path, include
from . import views
from knox import views as knox_views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/register/', views.register_user, name='register'),
    path('api/login/', views.login_user, name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
]


