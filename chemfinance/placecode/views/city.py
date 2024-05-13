# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from placecode.models import City,Country, State
from placecode.serializers.city import CitySerializer

@api_view(['GET', 'POST'])
def city(request):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response({'message' : 'success', 'status_code' : 200 , 'data' : serializer.data}, status= status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CitySerializer(data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'City is created successfully', 'status_code' : 201 , 'data' : serializer.data}, status= status.HTTP_201_CREATED)
        return Response({'message': 'error occured', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def city_update_delete(request,country_code: str, state_code: str, city_code: str):
    try:
        city = City.objects.get(city_code=city_code,country_code=country_code,state_code=state_code)
    except City.DoesNotExist:
        return Response({'message': 'City does not exist', 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CitySerializer(city)
        return Response({'message' : 'Success', 'status_code' : 200 , 'data' : serializer.data}, status= status.HTTP_200_OK)
    elif request.method =='PATCH':
        serializer = CitySerializer(city, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'City updated successfully', 'status_code' : 201 , 'data' : serializer.data}, status= status.HTTP_201_CREATED)
        return Response({'message': 'error occured', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        city.delete()
        return Response({'message': 'Deleted successfully', 'status_code': 204}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def city_list(request, country_code: str, state_code: str):
    # GET Method
    if country_code and state_code:
        cities = City.objects.filter(country_code=country_code, state__state_code = state_code)
        if cities.exists():
            serializer = CitySerializer(cities, many=True)
            return Response({'message' : 'Success', 'status_code' : 200 , 'data' : serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"error": "no city found for the provided state code",'status_code': 404}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "country code or state code not provided",'status_code': 400}, status=status.HTTP_400_BAD_REQUEST)
