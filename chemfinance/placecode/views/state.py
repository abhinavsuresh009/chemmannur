# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from placecode.models import State
from placecode.serializers.state import StateSerializer

@api_view(['GET', 'POST'])
def state(request):
    if request.method == 'GET':
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response({'message' : 'Success', 'status_code' : 200 , 'data' : serializer.data}, status= status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = StateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'State created successfully', 'status_code' : 201 , 'data' : serializer.data}, status= status.HTTP_201_CREATED)
        return Response({'message': 'error occured', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def state_update_delete(request, country_code: str, state_code: str):
    serializer = None  # Initialize serializer variable

    try:
        state = State.objects.get(country=country_code, state_code=state_code)
    except State.DoesNotExist:
        return Response({'message': 'error occurred', 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StateSerializer(state)
        return Response({'message': 'Success', 'status_code': 200, 'data': serializer.data}, status=status.HTTP_200_OK)

    elif request.method == 'PATCH':
        serializer = StateSerializer(state, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'State updated successfully', 'status_code': 201, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': 'error occurred', 'status_code': 400, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        state.delete()
        return Response({'message': 'Deleted successfully', 'status_code': 204}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def state_list(request, country_code: str):
    # GET Method
    if country_code:
        states = State.objects.filter(country=country_code)
        if states.exists():
            serializer = StateSerializer(states, many=True)
            return Response({'message' : 'Success', 'status_code' : 200, 'data' : serializer.data}, status= status.HTTP_200_OK)
        else:
            return Response({"error": "no states found for the provided country code"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({"error": "country code not provided"}, status=status.HTTP_400_BAD_REQUEST)