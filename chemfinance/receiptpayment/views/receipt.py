from rest_framework.decorators import api_view
from rest_framework.response import Response
from receiptpayment.models import ReceiptPayment
from receiptpayment.serializers.payment import PaymentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def reciept_list(request):
    if request.method == 'GET':
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        transaction_type = request.query_params.get('transaction_type', None)
        if start_date:
            queryset = ReceiptPayment.objects.filter(trdate__gte=start_date, trdate__lte=end_date, type = transaction_type)
        serializer = PaymentSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(type = 'Cash')
            return Response({'message' : 'Receipt create successfully', 'status_code' : '200' , 'data' : serializer.data} , status=status.HTTP_201_CREATED)
        return Response({'message' : 'Error found', 'status_code' : '400' , 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

