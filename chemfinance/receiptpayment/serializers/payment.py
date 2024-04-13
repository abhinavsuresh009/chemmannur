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

        if transaction_type == 'Cheque' and (debit is not None):
            raise serializers.ValidationError("Debit must be null for payment transactions.")
        
        if transaction_type == 'Cash' and (credit is not None):
            raise serializers.ValidationError("Credit must be null for receipt transactions.")

        if transaction_type == 'Cheque' and (debit is None and credit is None):
            raise serializers.ValidationError("Either debit or credit must be provided for payment transactions.")

        return data


    