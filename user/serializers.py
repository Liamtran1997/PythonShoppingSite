from rest_framework.serializers import ModelSerializer
from .models import User, User_Detail
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ['id', 'username', 'email', 'is_deleted']


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ['id', 'username', 'password', 'email', 'is_deleted']
        extra_kwargs = {
            'password': {'write_only': 'true'}
            # chỉ hiển thị khi nhập vào chứ ko show ra client
        }

        def create(self, validated_data):
            user = User()
            user.username = validated_data['username']
            user.set_password(validated_data['password'])
            user.email = validated_data['email']
            user.is_deleted = validated_data['is_deleted']
            user.save()

            return user


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User_Detail
        fields = ['user_id', 'fullname', 'phone', 'gender', 'address']




