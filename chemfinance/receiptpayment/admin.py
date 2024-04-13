from django.contrib import admin
from .models import ReceiptPayment, BankEntry
# Register your models here.
admin.site.register(ReceiptPayment)
admin.site.register(BankEntry)