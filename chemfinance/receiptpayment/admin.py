from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ReceiptPayment)
admin.site.register(BankEntry)
admin.site.register(Daybook)
admin.site.register(FingerImage)
admin.site.register(TypeOfTransaction)