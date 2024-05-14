from rest_framework import serializers
from receiptpayment.models import Daybook

class DaybookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daybook
        fields = '__all__'
