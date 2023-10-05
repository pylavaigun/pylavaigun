from django.contrib.auth.models import update_last_login
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegistrationSerializer, LoginSerializer

from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model

from .serializers import RegistrationSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = RegistrationSerializer
# Create your views here.


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer
    http_method_names = ['get', 'head', 'post']