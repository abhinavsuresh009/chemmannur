from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from receiptpayment.models import Daybook
from receiptpayment.serializers.daybook import DaybookSerializer
from django.utils import timezone
from receiptpayment.utils.util import save_receipt_payment_data  



@api_view(['GET'])
def daybook_list(request):
    if request.method == 'GET':
        daybooks = Daybook.objects.all()
        serializer = DaybookSerializer(daybooks, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def approve_daybook(request, daybook_id: str ):
    try:
        daybook = Daybook.objects.get(id=daybook_id)
    except Daybook.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if daybook.approved:
        return Response({"detail": "Already approved"}, status=status.HTTP_400_BAD_REQUEST)

    daybook.approved = True
    daybook.approvedby = '123'
    daybook.approvedtime = timezone.now()
    daybook.save()

    serializer = DaybookSerializer(daybook)
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['POST'])
def reciept_payment(request):
    serializer = DaybookSerializer(data=request.data)
    if serializer.is_valid():
        # Extract validated data
        validated_data = serializer.validated_data
        # Call save_receipt_payment_data with validated data
        return save_receipt_payment_data(serializer_class=DaybookSerializer, data=validated_data)
    # Return errors if serializer is not valid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


