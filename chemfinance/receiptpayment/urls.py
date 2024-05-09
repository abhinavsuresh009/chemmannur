# urls.py

from django.urls import path
from receiptpayment.views.receiptpayment import my_view
from receiptpayment.views.payment import payment
from receiptpayment.views.receipt import reciept
from receiptpayment.views.bank import bank

urlpatterns = [
    path('receiptpayments/', my_view, name='receiptpayments'),
    path('receipt/',reciept, name='receipt'),
    path('payment/',payment, name='payment'),
    path('bank/', bank),
]
