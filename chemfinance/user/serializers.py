from rest_framework import serializers
from . models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
    def validate(self, attrs):
        email = attrs.get('email', '').strip().lower()
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError("User with same email id already exists..")
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        
# class UpdateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"
    
#     def update(self, instance, validated_data):
#         password = validated_data.pop("password")
#         if password:
#             instance.set_password(password)
#         instance = super().update(instance,validated_data)
#         return instance

class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, write_only=True)

    def update(self, instance, validated_data):
        # Update the password for the user instance
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def validate_password(self, value):
        # Here you can add custom validation for the password if needed
        return value
    

# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(style={'input_type': 'password'})
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                # Retrieve or create a token for the user
                token, created = Token.objects.get_or_create(user=user)
                attrs['user'] = user
                attrs['token'] = token
                return attrs
            else:
                raise serializers.ValidationError('Invalid credentials', code='authorization')
        else:
            raise serializers.ValidationError('Must include "username" and "password"', code='authorization')