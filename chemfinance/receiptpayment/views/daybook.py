from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from receiptpayment.models import Daybook
from receiptpayment.serializers.daybook import DaybookSerializer

@api_view(['GET'])
def daybook_list(request):
    if request.method == 'GET':
        daybooks = Daybook.objects.all()
        serializer = DaybookSerializer(daybooks, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def approve_daybook(request, daybook_id: str):
    try:
        daybook = Daybook.objects.get(id=daybook_id)
    except Daybook.DoesNotExist:
        return Response({"error": "Daybook not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = DaybookSerializer(daybook, data={'approved': True}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
