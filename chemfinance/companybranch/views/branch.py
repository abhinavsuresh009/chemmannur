from rest_framework.decorators import api_view
from rest_framework.response import Response
from companybranch.models import Branch
from companybranch.serializers.branch import BranchSerializer
from rest_framework import status
from django.db import IntegrityError
from django.http import JsonResponse

# Views for Branch

@api_view(['GET','POST'])
def branch(request, comcode: str):
# GET Method
        branch = Branch.objects.filter(company=comcode)
        serializer = BranchSerializer(branch, many=True)
        return Response({'message' : 'Here is your Data', 'status_code' : 200 , 'data' : serializer.data}, status= status.HTTP_200_OK)
# POST Method
@api_view(['POST'])
def create_branch(request):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'All the best Branch is created successfully', 'status_code' : 201 , 'data' : serializer.data}, status= status.HTTP_201_CREATED)
        return Response({'message' : 'Check before submit', 'status_code' : 400 , 'data' : serializer.data}, status= status.HTTP_400_BAD_REQUEST)
    # DELETE and UPDATE Method      
@api_view(['PATCH', 'DELETE'])
def branch_delete_update(request):
    brcode = request.query_params.get('brcode', None)
    
    if not brcode:
        return Response({'message': 'brcode parameter is required for DELETE/PATCH method', 'status_code': 400}, status=status.HTTP_400_BAD_REQUEST)

    try:
        branch = Branch.objects.get(brcode=brcode)
    except Branch.DoesNotExist:
        return Response({'message': 'Branch not found', 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        branch.delete()
        return Response({'message': 'Deleted successfully', 'status_code': 204 }, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        serializer = BranchSerializer(branch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated successfully', 'status_code': 201, 'data': serializer.data}, status= status.HTTP_201_CREATED)
        return Response({'message': 'Error found', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
