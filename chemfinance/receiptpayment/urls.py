# urls.py

from django.urls import path
from receiptpayment.views.receiptpayment import my_view
from receiptpayment.views.payment import *
from receiptpayment.views.receipt import reciept
from receiptpayment.views.bank import bank
from receiptpayment.views.daybook import *

urlpatterns = [
    path('receiptpayments/', my_view, name='receiptpayments'),
    path('receipt/',reciept, name='receipt'),
    path('payment/',payment, name='payment'),
    path('bank/', bank),
    path('finger-image/', finger_image),
    path('daybooks/', daybook_list, name='daybook-list'),
    path('image/<str:image_id>/', image),
    path('daybooks/approve/<str:daybook_id>/', approve_daybook, name='approve-daybook'),

]
