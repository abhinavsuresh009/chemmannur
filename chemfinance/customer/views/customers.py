from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from customer.serializer.customerserializer import *
from customer.models import Customer
from companybranch.models import Branch, Company
from rest_framework import status
from django.db.models import Q
from rest_framework.parsers import MultiPartParser
from rest_framework.pagination import PageNumberPagination

# Post and GET Method for Customer
@api_view(['POST','GET'])  # saving application
def register_customer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "customer created successfully.", 'status_code': 201, "data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "error occured", 'status_code': 400,'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({'message':'success','status_code': 200,'data':serializer.data}, status=status.HTTP_200_OK)
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

# @api_view(['GET'])
# def search_customer(request, comcode: str, brcode: str): 
#     customer_name = request.query_params.get('customer_name')
#     customer_id = request.query_params.get('customer_id')
#     aadhaar = request.query_params.get('aadhaar')
#     query = (Q(comcode=comcode) & Q(brcode=brcode))
#     if comcode != comcode or brcode != brcode:
#         return Response({"message": "Invalid company code or branch code.", 'status_code': 400}, status=status.HTTP_400_BAD_REQUEST)   

#     elif customer_id or customer_name or aadhaar:
#         if customer_name:
#             customers = Customer.objects.filter(query,fname__istartswith=customer_name).order_by("trdate")
#         elif customer_id:
#             customers = Customer.objects.filter(query,cusid=customer_id).order_by("trdate")
#         elif aadhaar:
#             customers = Customer.objects.filter(query,aadhaar=aadhaar).order_by("trdate")
#         serializer = CustomerGetNameSerializer(customers, many=True)
#         if not customers:
#             return Response({"message": "please provide a valid Name or Id or Aadhaar.", 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)
#         return Response({"message": "success.", 'status_code': 200, "data":serializer.data}, status=status.HTTP_200_OK)    

# filter Customer by company code
@api_view(['GET'])
def filter_by_comcode(request, comcode: str):
    try:
        brcode = request.query_params.get('brcode',None)
        customer_name = request.query_params.get('customer_name', None)
        company_code = Company.objects.filter(comcode=comcode)
        branch_code = Branch.objects.filter(brcode=brcode)
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        if company_code:
            customers = Customer.objects.filter(comcode=comcode).order_by('-trdate')
        if branch_code:
            customers = customers.filter(brcode=brcode).order_by('-trdate')
        if customer_name:
            customers = customers.filter(fname__istartswith=customer_name).order_by("-trdate")
        if start_date and end_date:
            customers = customers.filter(trdate__gte=start_date, trdate__lte=end_date).order_by('-trdate')
        if not customers.exists():
            return Response({"error": "No customers found.", 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)
        # pagination
        paginator = PageNumberPagination()
        paginator.page_size = 2  # Number of items per page
        result_page = paginator.paginate_queryset(customers, request)
        serializer = CustomerSerializer(result_page, many=True)
        return paginator.get_paginated_response({"success": "filtered success.", 'status_code': 200, "data":serializer.data})
    except:
        return Response({"error": "server error", 'status_code': 500}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        

# search Customer with  customer_id or customer_name or Aadhar number
@api_view(['GET'])
def search_customer(request, comcode: str, brcode: str):     
    # Proceed with filtering customers only if comcode and brcode are provided and not empty
    query = Q(comcode=comcode, brcode=brcode)
    if not Company.objects.filter(comcode=comcode).exists():
        return Response({"error": "invalid comcode or brcode.", 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)
    if not Branch.objects.filter(brcode=brcode).exists():
        return Response({"error": "invalid comcode or brcode.", 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)
    customer_name = request.query_params.get('customer_name')
    customer_id = request.query_params.get('customer_id')
    aadhaar = request.query_params.get('aadhaar')
    if customer_name or customer_id or aadhaar:
        if customer_name:
            customers = Customer.objects.filter(query,fname__istartswith=customer_name).order_by("trdate")
        elif customer_id:
            customers = Customer.objects.filter(query,cusid=customer_id).order_by("trdate")
        elif aadhaar:
            customers = Customer.objects.filter(query,aadhaar=aadhaar).order_by("trdate")
        
        if not customers.exists():
            return Response({"error": "No customers found.", 'status_code': 404}, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerGetNameSerializer(customers, many=True)
        return Response({"success": "filtered success.", 'status_code': 200, "data":serializer.data}, status=status.HTTP_200_OK)    
    else:
        return Response({"error": "Please provide at least one filtering parameter (customer_name, customer_id, or aadhaar).", 'status_code': 400}, status=status.HTTP_400_BAD_REQUEST)
# upload image view
@api_view(['POST'])
@parser_classes([MultiPartParser])
def image_upload_view(request):
    if request.method == 'POST':
        file_serializer = ImageSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response({"message": "image added successfully.", 'status_code': 201, "data":file_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "error occured", 'status_code': 400,'error':file_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)