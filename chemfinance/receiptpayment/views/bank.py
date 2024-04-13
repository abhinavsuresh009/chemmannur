from rest_framework.decorators import api_view
from rest_framework.response import Response
from receiptpayment.models import BankEntry
from receiptpayment.serializers.bank import BankSerializer
from datetime import datetime
from rest_framework import status



@api_view(['POST'])
def bank_list(request):
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Create successfully', 'status_code' : '200' , 'data' : serializer.data}, status=status.HTTP_200_OK )
        else:
            return Response({'message' : 'Error found', 'status_code' : '400' , 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
