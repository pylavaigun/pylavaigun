from django.contrib.auth.models import update_last_login
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegistrationSerializer, CustomTokenObtainPairSerializer

from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model

from .serializers import RegistrationSerializer


#FRONTEND
#Main page
def index(request):
    user = request.user
    data = {
        'user': user,
        'test': 'test_data'
    }
    template = 'index.html'
    return render(request, template, context=data)

#Login page

def login_page(request):
    template = 'login_page.html'
    return render(request, template)



#BACKEND

#Create new user
class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = RegistrationSerializer


#Authentication
class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer
    http_method_names = ['get', 'head', 'post']

