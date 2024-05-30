from rest_framework import serializers
from goldloan.models import GoldLoan

# Serializer for Goldloan
class GoldLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoldLoan
        fields = '__all__'
        
