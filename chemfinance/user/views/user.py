from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from user.serializers.changepasswordserializer import ChangePasswordSerializer
from user.serializers.userserializer import CreateUserSerializer
from rest_framework.permissions import IsAuthenticated


# Change Password Views

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.update_password(request.user, serializer.validated_data)
        return Response({"message": "Password updated successfully.", 'status_code': 201}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Error Occurred', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Create User Views

@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == 'POST':
        # requesting data from serializer
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Successfully Created','status_code': 201,'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Error Occur','status_code': 400,'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        users = User.objects.all()
        serializer = CreateUserSerializer(users, many=True)
        return Response({'message':'Here is the details','status_code': 200,'data':serializer.data}, status=status.HTTP_200_OK)
