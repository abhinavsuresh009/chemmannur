# urls.py

from django.urls import path
from receiptpayment.views.receiptpayment import my_view
from receiptpayment.views.payment import payment_list
from receiptpayment.views.receipt import reciept_list
from receiptpayment.views.bank import bank_list

urlpatterns = [
    path('receiptpayments/', my_view, name='receiptpayments'),
    path('receipt_list/',reciept_list, name='receipt-list'),
    path('payment_list/',payment_list, name='payment-list'),
    path('banks/', bank_list),
]
