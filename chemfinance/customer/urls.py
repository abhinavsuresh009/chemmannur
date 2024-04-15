from django.urls import path
from customer.views.customers import *
urlpatterns = [
    path('', register_customer),
    # path('get-branch-customer/<str:comcode>/<str:brcode>/<str:customer_name>', get_customer_by_name),
    # path('get-customer/<str:comcode>/<str:brcode>/<str:customer_id>', get_customer_by_id),
    path('get_customer/<str:comcode>/<str:brcode>/', get_customer),

]