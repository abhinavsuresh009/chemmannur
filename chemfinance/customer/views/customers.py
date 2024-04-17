from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer.serializer.customerserializer import *
from customer.models import Customer
from rest_framework import status
from django.db.models import Q


# Post and GET Method for Customer

@api_view(['POST','GET'])  # saving application
def register_customer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Created successfully.", 'status_code': 201, "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to save.", 'status_code': 400,'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({'message':'Here is the details','status_code': 200,'data':serializer.data}, status=status.HTTP_200_OK)
# @api_view(['GET'])  # serching by name
# def get_customer_by_name(request,comcode: str, brcode: str, customer_name: str):
#     #customer = Customer.objects.filter(comcode=comcode,brcode = brcode,fname__icontains = customer_name).order_by("trdate")
#     #serching foor all fname start with character
#     customer = Customer.objects.filter(comcode=comcode,brcode = brcode,fname__istartswith = customer_name).order_by("trdate")
#     customer_serializer = CustomerGetNameSerializer(customer, many = True)
#     return Response({"message": "Success", "data": customer_serializer.data }, status=200)

# @api_view(['GET'])  # geting by customer id
# def get_customer_by_id(request,comcode: str, brcode: str, customer_id: str):
#     customer = Customer.objects.filter(comcode=comcode,brcode = brcode,cusid = customer_id).first()
#     print(customer)
#     if not customer:
#         return Response({'error':'Not found'},status=400)
#     customer_serializer = CustomerSerializer(customer)
#     return Response({"message": "Success", "data": customer_serializer.data }, status=200)

# # Search by NAME and ID Function

@api_view(['GET'])
def search_customer(request, comcode: str, brcode: str):    
    customer_name = request.query_params.get('customer_name')
    customer_id = request.query_params.get('customer_id')
    if customer_id or customer_name:
        query = (Q(comcode=comcode) & Q(brcode=brcode))
        if customer_name:
            customers = Customer.objects.filter(query,fname__icontains=customer_name).order_by("trdate")
        elif customer_id:
            customers = Customer.objects.filter(query,cusid=customer_id).order_by("trdate")
        if not customers:
            return Response({"message": "Customer not found.", 'status_code': 404,'error':serializer.errors}, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerGetNameSerializer(customers, many=True)
        return Response({"message": "Here is your result.", 'status_code': 200, "data":serializer.data}, status=status.HTTP_200_OK)    
    return Response({"message": "Please provide a valid Name or Id.", 'status_code': 400,'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)# from django.db.models import Q
