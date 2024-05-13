from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from placecode.models import Country
from placecode.serializers.country import CountrySerializer

@api_view(['GET', 'POST'])
def country_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response({'message' : 'Success', 'status_code' : 200 , 'data' : serializer.data}, status= status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Country created successfully', 'status_code' : 201 , 'data' : serializer.data}, status= status.HTTP_201_CREATED)
        return Response({'message': 'error occured', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def country_update_delete(request, country_code: str):
    try:
        country = Country.objects.get(country_code=country_code)
    except Country.DoesNotExist:
        return Response({'message': 'error occured', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return Response({'message' : 'Success', 'status_code' : 200 , 'data' : serializer.data}, status= status.HTTP_200_OK)

    elif request.method in ['PUT', 'PATCH']:
        serializer = CountrySerializer(country, data=request.data, partial=request.method == 'PATCH')
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Country Updated successfully', 'status_code' : 201 , 'data' : serializer.data}, status= status.HTTP_201_CREATED)
        return Response({'message': 'error occured', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country.delete()
        return Response({'message': 'Deleted successfully', 'status_code': 204, 'error': serializer.errors}, status=status.HTTP_204_NO_CONTENT)
