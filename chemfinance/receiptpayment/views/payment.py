from rest_framework.decorators import api_view
from rest_framework.response import Response
from receiptpayment.models import ReceiptPayment, FingerImage
from receiptpayment.serializers.payment import PaymentSerializer,FingerSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def payment(request):
    if request.method == 'GET':
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        transaction_type = request.query_params.get('transaction_type', None)
        if start_date:
            queryset = ReceiptPayment.objects.filter(trdate__gte=start_date, trdate__lte=end_date, type = transaction_type)
            serializer = PaymentSerializer(queryset, many=True)
            return Response({'message' : 'success', 'status_code' : 200 , 'data' : serializer.data} , status=status.HTTP_200_OK)
        return Response({'error' : 'error occured', 'status_code' : 400}, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(type = 'P')
            return Response({'message' : 'Payment created successfully', 'status_code' : 201 , 'data' : serializer.data} , status=status.HTTP_201_CREATED)
        return Response({'message' : 'error occured', 'status_code' : 400 , 'error' : serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def finger_image(request):
    
        
    if request.method == 'POST':
        serilaizer = FingerSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data)
        return Response(status=400)
@api_view(['GET'])
def image(request, image_id: str):
    if request.method == 'GET':
        image = FingerImage.objects.get(id = image_id)
        serializer = FingerSerializer(image)
        return Response(serializer.data)
    return Response(status=400)
        
        
    