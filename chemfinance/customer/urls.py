from django.urls import path
from customer.views.customers import *
urlpatterns = [
    path('register-customer/', register_customer),
    # path('get-branch-customer/<str:comcode>/<str:brcode>/<str:customer_name>', get_customer_by_name),
    # path('get-customer/<str:comcode>/<str:brcode>/<str:customer_id>', get_customer_by_id),
    path('search-customer/<str:comcode>/<str:brcode>/', search_customer),
    path('filter-comcode/<str:comcode>/', filter_by_comcode),
    path('image/', image_upload_view),

]