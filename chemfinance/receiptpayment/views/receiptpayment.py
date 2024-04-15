# from django.http import HttpResponse
from receiptpayment.utils.util import save_receipt_payment_data  
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from receiptpayment.serializers.receiptpayment import ReceiptPaymentSerializer

@api_view(['POST'])
def my_view(request):
    if request.method == 'POST':
        data = request.data
        return save_receipt_payment_data(ReceiptPaymentSerializer, data)

    return Response({'error': 'Method not allowed', "status_code": 405}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
 

