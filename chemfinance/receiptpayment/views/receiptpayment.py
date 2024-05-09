# from django.http import HttpResponse
from receiptpayment.utils.util import save_receipt_payment_data  
from rest_framework.decorators import api_view
from receiptpayment.serializers.receiptpayment import ReceiptPaymentSerializer

@api_view(['POST'])
def my_view(request):
    data = request.data
    return save_receipt_payment_data(ReceiptPaymentSerializer, data)

 

