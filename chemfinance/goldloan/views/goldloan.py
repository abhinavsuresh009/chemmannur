from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date as dt
from goldloan.models import GoldLoan
from goldloan.serializers.goldloan import GoldLoanSerializer
from rest_framework import status

# GET Method for closed loans

@api_view(['GET'])
def closed_loans(request):
    date = request.query_params.get('date')
    try:
        date = dt.fromisoformat(date)
    except ValueError:
        return Response({"message": "Invalid date format. Use YYYY-MM-DD.", 'status_code': 400,'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    closed_loans = GoldLoan.objects.filter(closed=True, Closed_date__year=date.year, Closed_date__month = date.month)
    serializer = GoldLoanSerializer(closed_loans, many=True)

    return Response({'message':'Here is the details','status_code': 200,'data':serializer.data}, status=status.HTTP_200_OK)
# GET Method for Pending loans

@api_view(['GET'])
def pending_loan(request):
    date = request.query_params.get('date')
    try:
        date = dt.fromisoformat(date)
    except ValueError:
        return Response({"message": "Invalid date format. Use YYYY-MM-DD.", 'status_code': 400,'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    pending_loans = GoldLoan.objects.filter(closed=False, Closed_date__lte= date)
    serializer = GoldLoanSerializer(pending_loans, many=True)

    return Response({'message':'Here is the details','status_code': 200,'data':serializer.data}, status=status.HTTP_200_OK)

