# serializers.py
from rest_framework import serializers
from receiptpayment.models import AccountingHead

class AccountingHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountingHead
        fields = ['id', 'head_code', 'grouphead_id', 'name']
