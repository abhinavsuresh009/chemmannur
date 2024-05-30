# views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from receiptpayment.models import AccountingHead, VoucherHead
from receiptpayment.serializers.voucherhead import VoucherHeadSerializer

@api_view(['POST', 'GET'])
def create_voucher_head(request):
    if request.method == 'POST':
        serializer = VoucherHeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'voucher created successfully', 'status_code' : 201 , 'data' : serializer.data} , status=status.HTTP_201_CREATED)
        return Response({'message' : 'error occured', 'status_code' : 400 , 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        queryset = VoucherHead.objects.all()
        serializer = VoucherHeadSerializer(queryset, many=True)
        return Response({'message' : 'success', 'status_code' : 200 , 'data' : serializer.data} , status=status.HTTP_200_OK)
    return Response({'error' : 'error occured', 'status_code' : 400}, status=status.HTTP_400_BAD_REQUEST)

