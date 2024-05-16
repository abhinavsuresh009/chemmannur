from rest_framework import serializers
from receiptpayment.models import Daybook


# Serializer for payment 

class ReceiptSerializer(serializers.ModelSerializer):
    type = serializers.CharField(default='R')
    credit = serializers.FloatField(default=0, required=False, read_only = True)
    class Meta:
        model = Daybook
        fields = '__all__'
