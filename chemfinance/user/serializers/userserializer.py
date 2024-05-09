from rest_framework import serializers
from user.models import User
from companybranch.models import Company, Branch
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only = True)
    # condition for phone number
    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'email', 'phone', 'comcode', 'brcode']
        
    def validate(self, attrs):
        # giving conditions to username
        brcode = attrs['brcode']
        comcode = attrs['comcode']
        username = attrs['username']
        if not Company.objects.filter(comcode=comcode).exists():
            raise serializers.ValidationError({"comcode": "Company code does not exist."})
        if not Branch.objects.filter(company=comcode, brcode=brcode).exists():
            raise serializers.ValidationError({"brcode" : "Branch code is not within the company."})

        if len(username) == 3:
            raise serializers.ValidationError({"username" : "Username must have a 3 characters"})
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password', None)
        # Check if password and confirm_password match
        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match"})
        # giving conditions to password
        password = attrs.get('password')
        if len(password) < 4:
            raise serializers.ValidationError({"password" : "Password must have a minimum of 4 characters."})
        return attrs
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('confirm_password', None)

        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
        
