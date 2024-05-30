from rest_framework.decorators import api_view
from rest_framework.response import Response
from goldloan.serializers.natureofloan import NatureOfLoanSerializer
from goldloan.models import NatureOfLoan
from rest_framework import status


@api_view(['GET'])
def nature_loans(request):
# GET Method
    if request.method == 'GET':
        loans = NatureOfLoan.objects.all()
        serializer = NatureOfLoanSerializer(loans, many=True)
        return Response({'message' : 'success', 'status_code' : 200 , 'data' : serializer.data}, status= status.HTTP_200_OK)