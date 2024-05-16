from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from receiptpayment.models import TypeOfTransaction
from receiptpayment.serializers.typeoftransaction import TypeOfTransactionSerializer

@api_view(['GET'])
def transaction_list_create(request):
    if request.method == 'GET':
        transactions = TypeOfTransaction.objects.all()
        serializer = TypeOfTransactionSerializer(transactions, many=True)
        return Response({"success": "Method payment fetched successfully.", 'status_code': 200, "data": serializer.data})
    return Response({"error": "Server error occurred.", 'status_code': 500}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
