# from django.shortcuts import render
# from rest_framework.generics import CreateAPIView, UpdateAPIView
# from .models import User
# from .serializers import CreateUserSerializer, UpdateUserSerializer



# Create your views here.
# class CreateUserAPI(CreateAPIView):
#     user = User.objects.all()
#     serializer_class = CreateUserSerializer

# class UpdateUserAPI(UpdateAPIView):
#     user = User.objects.all()
#     serializer_class = UpdateUserSerializer



from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework import status
from .models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .serializers import CreateUserSerializer, UpdatePasswordSerializer, UserLoginSerializer

@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = CreateUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '','status_code': 201,'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': '','status_code': 400,'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        users = User.objects.all()
        serializer = CreateUserSerializer(users, many=True)
        return Response({'message':'','status_code': 201,'data':serializer.data})

# @api_view(['GET', 'PATCH'])
# def update_user(request, pk):
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PATCH':
#         serializer = UpdateUserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'GET':
#         serializer = UpdateUserSerializer(user)
#         return Response(serializer.data)

@api_view(['PATCH', 'GET'])
def update_password(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = UpdatePasswordSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        users = User.objects.all()
        serializer = CreateUserSerializer(users, many=True)
        return Response({'message':'','status_code': 201,'data':serializer.data})
    

# @api_view(['POST'])
# def user_login(request):
#     if request.method == 'POST':
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 # Retrieve or create a token for the user
#                 token, created = Token.objects.get_or_create(user=user)
#                 return Response({'token': token.key}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token = serializer.validated_data['token']
            return Response({'message' : 'User logged in  successfully', 'status_code' : '200' , 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)