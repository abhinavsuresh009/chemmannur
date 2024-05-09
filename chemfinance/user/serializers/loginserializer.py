from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


# User Login Serializer

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']
        # checking username and password
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                # Retrieve or create a token for the user
                token, created = Token.objects.get_or_create(user=user)
                attrs['user'] = user
                attrs['token'] = token
                return attrs
            else:
                raise serializers.ValidationError({'password':'Invalid Username or Password'}, code='authorization')
        else:
            raise serializers.ValidationError({"password" : 'Must include "username" and "password"'}, code='authorization')
        
