from rest_framework import serializers
from companybranch.models import Company

# Serializer for Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

        
        