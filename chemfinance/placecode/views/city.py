# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from placecode.models import City,Country, State
from placecode.serializers.city import CitySerializer

@api_view(['GET', 'POST'])
def city_list(request):
    if request.method == 'GET':
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        country_code = request.data.get('country_code')
        state_code = request.data.get('state_code')
        city_code = request.data.get('city_code')

        # Validate country code
        
        # Validate state code
        try:
            state = State.objects.filter(country=country_code, state_code=state_code)
        except State.DoesNotExist:
            return Response({"state_code": "State with this code does not exist in the provided country."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check if city code already exists in the provided state
        if City.objects.filter(state=state, city_code=city_code).exists():
            return Response({"city_code": "A city with this city code already exists in the provided state."}, status=status.HTTP_400_BAD_REQUEST)

        # If all validation passes, you can process the data further
        # For example, save the data to the database
        serializer = CitySerializer(data=request.data)


    # Handle other HTTP methods if necessary
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def city_detail(request,country_code: str, state_code: str, city_code: str):
    try:
        city = City.objects.get(city_code=city_code,country_code=country_code,state_code=state_code)
    except City.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CitySerializer(city)
        return Response(serializer.data)

    elif request.method =='PATCH':
        serializer = CitySerializer(city, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        city.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
