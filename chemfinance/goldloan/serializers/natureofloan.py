from rest_framework import serializers
from goldloan.models import NatureOfLoan

class NatureOfLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = NatureOfLoan
        fields = '__all__'
