from rest_framework import serializers
from receiptpayment.models import ReceiptPayment


class ReceiptPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptPayment
        fields = ['gcode', 'comcode', 'brcode', 'ucode', 'description', 'hcode', 'hcode1', 'name', 'code',
                  'credit', 'debit', 'vono', 'type', 'chkdate', 'chkno', 'bank', 'ifsc', 'acno', 'mode']


