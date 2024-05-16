from rest_framework import serializers
from receiptpayment.models import FingerImage, Daybook


# Serializer for payment 

class PaymentSerializer(serializers.ModelSerializer):
    type = serializers.CharField(default='P')
    debit = serializers.FloatField(default=0, required=False, read_only = True)
    class Meta:
        model = Daybook
        fields = '__all__'
        
        
    
            
class FingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FingerImage
        fields = '__all__'


    