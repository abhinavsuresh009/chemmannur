from rest_framework.decorators import api_view
from rest_framework.response import Response
from companybranch.models import Branch
from companybranch.serializers.branch import BranchSerializer
from rest_framework import status


# Views for Branch

@api_view(['GET','POST'])
def branch(request):
# GET Method
    comcode = request.query_params.get('comcode', None)
    if request.method == 'GET':
        companies = Branch.objects.all()
        serializer = BranchSerializer(companies, many=True,context = {'comcode' : comcode})
        return Response({'message' : 'Here is your Data', 'status_code' : '200' , 'data' : serializer.data})
    
# POST Method
    elif request.method == 'POST':
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Create successfully', 'status_code' : '200' , 'data' : serializer.data}, status=status.HTTP_200_OK )
        else:
            return Response({'message' : 'Error found', 'status_code' : '400' , 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)        
@api_view(['PATCH', 'DELETE'])
def branch_delete_update(request):
    brcode = request.query_params.get('brcode', None)
    
    if not brcode:
        return Response({'message': 'brcode parameter is required for PUT/PATCH method', 'status_code': '400'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        branch = Branch.objects.get(brcode=brcode)
    except Branch.DoesNotExist:
        return Response({'message': 'Branch not found', 'status_code': '404'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        branch.delete()
        return Response({'message': 'Deleted successfully', 'status_code': '200'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        serializer = BranchSerializer(branch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated successfully', 'status_code': '200', 'data': serializer.data})
        return Response({'message': 'Error found', 'status_code': '400', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
