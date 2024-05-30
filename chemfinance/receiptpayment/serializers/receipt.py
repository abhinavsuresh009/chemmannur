from rest_framework import serializers
from receiptpayment.models import Daybook


# Serializer for payment 

class ReceiptSerializer(serializers.ModelSerializer):
    type = serializers.CharField(read_only=True)
    debit = serializers.FloatField(default=0, required=False, read_only = True)
    voucher_no = serializers.IntegerField(read_only=True)
    class Meta:
        model = Daybook
        fields = '__all__'
        
    def validate(self, attrs):
        mode = attrs.get('mode')
        
        if mode == 'cash':
            attrs['type'] = 'C'
        else:
            attrs['type'] = 'Q'
        
        return super().validate(attrs)
                

    def create(self, validated_data):
        existing_receipts_count = Daybook.objects.count()
        next_voucher_number = existing_receipts_count + 1
        validated_data['voucher_no'] = next_voucher_number
        return super().create(validated_data)