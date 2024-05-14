from django.contrib import admin
from .models import ReceiptPayment, BankEntry,Daybook,FingerImage
# Register your models here.
admin.site.register(ReceiptPayment)
admin.site.register(BankEntry)
admin.site.register(Daybook)
admin.site.register(FingerImage)