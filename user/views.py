from django.shortcuts import render, HttpResponse
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, generics, permissions
from .models import User, User_Detail
from .serializers import UserSerializer, RegisterUserSerializer
from knox.models import AuthToken
from .services import LoginAPI, RegisterAPI
from django.contrib.auth import login
# Create your views here.


# @api_view(['POST'])
# def register_user(request, *args, **kwargs):
#     return RegisterAPI.post(request, *args, **kwargs)
#
#
# @api_view(['POST'])
# def login_user(request):
#     return LoginAPI.post(request)


class UserViewSet(viewsets.ViewSet,
                  generics.ListAPIView,
                  generics.CreateAPIView,):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer



