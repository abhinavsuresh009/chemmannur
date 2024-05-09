from rest_framework import serializers
from django.contrib.auth.hashers import check_password
#Change Password Serializer
class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        request = self.context.get('request')
        user = request.user if request else None 
        if user:
            current_password = data.get('current_password')
            # Check if the current password provided matches the user's actual password
            if not user.check_password(current_password):
                raise serializers.ValidationError({"current_password": "The current password is incorrect."})
        # Check if new password and confirm new password match
        if data.get('new_password') != data.get('confirm_password'):
            raise serializers.ValidationError({"confirm_password" : "New password and confirm new password must match."})
        elif data.get('current_password') == data.get('new_password'):
            raise serializers.ValidationError({"new_password": "Both current password and new password are same"})
        # Check if the new password meets the length requirement
        new_password = data.get('new_password')
        if len(new_password) < 4:
            raise serializers.ValidationError({"new_password" : "Password must have a minimum of 4 characters.",'status_code': 400})
        return data

    def update_password(self, user, validated_data):
        new_password = validated_data.get('new_password')        
        user.set_password(new_password)
        user.save()

