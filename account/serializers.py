from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User

from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate  # If used custom user model

UserModel = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ("email", "username", "password", )




class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],
                                   username=validated_data['username'],
                                   password=validated_data['password'],

                                   )
        user.set_password(validated_data['password'])
        user.save()
        return user




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': self.user.username})
        data.update({'email': self.user.email})
        data.update({'id': self.user.id})
        # and everything else you want to send in the response
        return data
