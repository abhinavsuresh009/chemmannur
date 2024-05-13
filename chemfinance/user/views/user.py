from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from user.serializers.changepasswordserializer import ChangePasswordSerializer
from user.serializers.userserializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


# Change Password Views
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.update_password(request.user, serializer.validated_data)
        return Response({"message": "password changed successfully.", 'status_code': 201}, status=status.HTTP_201_CREATED)
    else:
        return Response({"message":"error occured", 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
# Create User Views
@api_view(['GET', 'POST'])
def user(request):
    if request.method == 'POST':
        # requesting data from serializer
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'user successfully created','status_code': 201,'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': 'error occured','status_code': 400,'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        try:
            brcode = request.query_params.get('brcode',None)
            comcode = request.query_params.get('comcode', None)
            user_name = request.query_params.get('user_name', None)
            users = User.objects.all()
            if comcode:
                users = User.objects.filter(comcode= comcode)
            if brcode:
                users = users.filter(brcode=brcode)
            if user_name:
                users = users.filter(username__istartswith=user_name)
            if not users.exists():
                return Response({"error": "No customers found.", 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)
            # pagination
            paginator = PageNumberPagination()
            paginator.page_size = 4  # Number of items per page
            result_page = paginator.paginate_queryset(users, request)
            serializer = UserSerializer(result_page, many=True)
            return paginator.get_paginated_response({"success": "filtered success.", 'status_code': 200, "data":serializer.data})
        except:
            return Response({"error": "server error", 'status_code': 500}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
