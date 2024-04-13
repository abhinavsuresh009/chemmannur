from rest_framework import serializers


#Change Password Serializer


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        # Check if new password and confirm new password match
        if data.get('new_password') != data.get('confirm_password'):
            raise serializers.ValidationError({"password" : "New password and confirm new password must match."})
        if data.get('current_password') == data.get('new_password'):
            raise serializers.ValidationError({"Password": "Both current password and new password are same"})
        # Check if the new password meets the length requirement
        new_password = data.get('new_password')
        if len(new_password) < 3 or len(new_password) > 4:
            raise serializers.ValidationError({"password" : "Password must have a minimum of 3 characters and a maximum of 4 characters."})
        
        return data

    def update_password(self, user, validated_data):
        # Update user's password
        current_password = validated_data.get('current_password')
        new_password = validated_data.get('new_password')

        if not user.check_password(current_password):
            raise serializers.ValidationError({"password" : "The old password is incorrect."})
        
        user.set_password(new_password)
        user.save()

