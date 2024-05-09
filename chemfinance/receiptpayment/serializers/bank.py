from rest_framework import serializers
from receiptpayment.models import BankEntry



class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankEntry
        fields = '__all__'

   