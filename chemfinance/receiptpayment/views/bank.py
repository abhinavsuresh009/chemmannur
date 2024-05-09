from rest_framework.decorators import api_view
from rest_framework.response import Response
from receiptpayment.serializers.bank import BankSerializer
from rest_framework import status



@api_view(['POST'])
def bank(request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'bank create successfully', 'status_code' : 201 , 'data' : serializer.data}, status=status.HTTP_201_CREATED )
        else:
            return Response({'message' : 'error occured', 'status_code' : 400 , 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
