from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import GoldRate
from .serializers import GoldrateSerializer

@api_view(['POST'])
def goldrate(request):
    if request.method == 'POST':
        serializer = GoldrateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Created successfully", "status_code": 201, "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Error Found", "status_code": 400}, status=status.HTTP_400_BAD_REQUEST)
