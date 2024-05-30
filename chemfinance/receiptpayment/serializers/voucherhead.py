from rest_framework import serializers
from receiptpayment.models import VoucherHead

class VoucherHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoucherHead
        fields = "__all__"