from rest_framework.response import Response
from rest_framework import status

def save_receipt_payment_data(serializer_class, data):
    serializer = serializer_class(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'created successfully', 'status_code':201}, status=status.HTTP_201_CREATED)
    return Response({'error': 'error occured', 'status_code':400} , status=status.HTTP_400_BAD_REQUEST)

