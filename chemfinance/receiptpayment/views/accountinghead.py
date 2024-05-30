from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from receiptpayment.models import AccountingHead
from receiptpayment.serializers.accountinghead import AccountingHeadSerializer

@api_view(['GET', 'POST'])
def accounting_head_list(request):
    if request.method == 'GET':
        accounting_heads = AccountingHead.objects.all()
        serializer = AccountingHeadSerializer(accounting_heads, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AccountingHeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)