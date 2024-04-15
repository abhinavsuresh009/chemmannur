from rest_framework.decorators import api_view
from rest_framework.response import Response
from companybranch.models import Company
from companybranch.serializers.company import CompanySerializer
from rest_framework import status

# Views for Company

@api_view(['GET','POST'])
def company(request):

# GET Method
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response({'message' : 'Here is Your Data', 'status_code' : '200' , 'data' : serializer.data})
    
# POST Method
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Create successfully', 'status_code' : '200' , 'data' : serializer.data}, status=status.HTTP_200_OK )
        else:
            return Response({'message' : 'Error found', 'status_code' : '400' , 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['PATCH', 'DELETE'])
def company_delete_update(request):
    comcode = request.query_params.get('comcode', None)
    
    if not comcode:
        return Response({'message': 'comcode parameter is required for PUT/PATCH method', 'status_code': '400'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        branch = Company.objects.get(comcode=comcode)
    except Company.DoesNotExist:
        return Response({'message': 'Branch not found', 'status_code': '404'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        branch.delete()
        return Response({'message': 'Deleted successfully', 'status_code': '200'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        serializer = CompanySerializer(branch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated successfully', 'status_code': '200', 'data': serializer.data})
        return Response({'message': 'Error found', 'status_code': '400', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    
    
    
    
    
    
    
    
