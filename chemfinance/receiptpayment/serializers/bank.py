from rest_framework import serializers
from receiptpayment.models import BankEntry
from django.core.validators import RegexValidator



class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankEntry
        fields = '__all__'

   