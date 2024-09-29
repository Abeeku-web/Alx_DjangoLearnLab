from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password_confirm = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        """
        Check that the two password entries match.
        """
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')

        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        Token.objects.create(user=user)
        return user