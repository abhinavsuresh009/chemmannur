from rest_framework import serializers
from receiptpayment.models import TypeOfTransaction

class TypeOfTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfTransaction
        fields = ['id', 'payment_name']