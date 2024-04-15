from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from customer.serializer.customerserializer import *
from customer.models import Customer
from rest_framework import status



@api_view(['POST','GET'])  # saving application
def register_customer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Created successfully.", 'status_code': 201, "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to save.", 'status_code': 400}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
    #     # a=Customer.objects.all()
    #     # s=CustomerSerializer(a,many=True)
    #     # return Response(s.data,status=200)
    #     ...
        return Response(status=500)

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

@api_view(['GET'])
def get_customer(request, comcode: str, brcode: str):
    
    customer_name = request.query_params.get('customer_name')
    customer_id = request.query_params.get('customer_id')
    if customer_name:
        customers = Customer.objects.filter(comcode=comcode, brcode=brcode, fname__icontains=customer_name).order_by("trdate")
        serializer = CustomerGetNameSerializer(customers, many=True)
        return Response({"msg": "Success", "data": serializer.data}, status=200)   
    if customer_id:
        customer = Customer.objects.filter(comcode=comcode, brcode=brcode, cusid=customer_id).order_by("trdate")
        if not customer:
            return Response({"msg": "Customer not found"}, status=404)
        serializer = CustomerGetNameSerializer(customer, many = True)
        return Response({"msg": "Success", "data": serializer.data}, status=200)
    
    return Response({"msg": "Please provide a name or an id"}, status=400)
