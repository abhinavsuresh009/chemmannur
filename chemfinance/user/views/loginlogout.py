from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from user.serializers.loginserializer import UserLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# User login view
@api_view(['POST'])
def user_login(request):
    
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            # storing user data and token to variables
            user = serializer.validated_data['user']
            token = serializer.validated_data['token']
            return Response({'message' : 'Logged in successfully', 'status_code' : 200 , 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Login failed','status_code': 400,'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# Logout Views
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    # Delete the token associated with the current user
    Token.objects.filter(user=request.user).delete()
    return Response({"message": "Logged out successfully.", "status_code": 204}, status=status.HTTP_204_NO_CONTENT)
