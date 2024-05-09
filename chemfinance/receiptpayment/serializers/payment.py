from rest_framework import serializers
from receiptpayment.models import ReceiptPayment


# Serializer for payment 

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptPayment
        fields = '__all__'
        
    def validate(self, data):
        transaction_type = data.get('type')
        debit = data.get('debit')
        credit = data.get('credit')

        if transaction_type == 'Q' and (debit is not None):
            raise serializers.ValidationError({"error": "Debit must be null for payment transactions."})
        
        if transaction_type == 'C' and (credit is not None):
            raise serializers.ValidationError({"error": "Credit must be null for receipt transactions."})

        if transaction_type == 'Q' and (debit is None and credit is None):
            raise serializers.ValidationError({"error": "Either debit or credit must be provided for payment transactions."})

        return data


    