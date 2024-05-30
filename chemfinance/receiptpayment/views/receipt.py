from rest_framework.decorators import api_view
from rest_framework.response import Response
from receiptpayment.models import Daybook
from receiptpayment.serializers.receipt import ReceiptSerializer
from rest_framework import status
import random

@api_view(['GET', 'POST'])
def reciept(request):
    if request.method == 'GET':
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        transaction_type = request.query_params.get('transaction_type', None)
        if start_date:
            queryset = Daybook.objects.filter(trdate__gte=start_date, trdate__lte=end_date, type = transaction_type)
            serializer = ReceiptSerializer(queryset, many=True)
            return Response({'message' : 'success', 'status_code' : 200 , 'data' : serializer.data} , status=status.HTTP_200_OK)
        return Response({'error' : 'error occured', 'status_code' : 400}, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'POST':
        print('check', request.data)
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'receipt created successfully', 'status_code' : 201 , 'data' : serializer.data} , status=status.HTTP_201_CREATED)
        return Response({'message' : 'error occured', 'status_code' : 400 , 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

