from rest_framework.decorators import api_view
from rest_framework.response import Response
from companybranch.models import Company
from companybranch.serializers.company import CompanySerializer
from rest_framework import status

# Views for Company
@api_view(['GET'])
def company_details(request, comcode: str):
    try:
        company = Company.objects.get(comcode=comcode)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    except Company.DoesNotExist:
        return Response({"error": "Company not found", 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)
@api_view(['GET','POST'])
def company(request):
# GET Method
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response({'message' : 'success', 'status_code' : 200 , 'data' : serializer.data}, status= status.HTTP_200_OK)
    
# POST Method
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success' : 'company create successfully', 'status_code' : 201 , 'data' : serializer.data}, status=status.HTTP_201_CREATED )
        else:
            return Response({'error' : 'error occured', 'status_code' : 400 , 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
# DELETE and UPDATE Method
        
@api_view(['PATCH', 'DELETE'])
def company_delete_update(request):
    comcode = request.query_params.get('comcode', None)
    
    if not comcode:
        return Response({'error': 'comcode parameter is required for DELETE/PATCH method', 'status_code': 400}, status=status.HTTP_400_BAD_REQUEST)

    try:
        branch = Company.objects.get(comcode=comcode)
    except Company.DoesNotExist:
        return Response({'error': 'company not found', 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        branch.delete()
        return Response({'message': 'Deleted successfully', 'status_code': 204}, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PATCH':
        serializer = CompanySerializer(branch, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated successfully', 'status_code': 201, 'data': serializer.data}, status= status.HTTP_201_CREATED)
        return Response({'error': 'error occured', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    
    
    
    
    
    
    
    
