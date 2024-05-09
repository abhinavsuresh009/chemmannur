from rest_framework import serializers
from companybranch.models import Company

# Serializer for Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

        
    def validate(self, attrs):
        comcode = attrs['comcode']
        if not Company.objects.filter(comcode=comcode).exists():
            raise serializers.ValidationError({"comcode" : "Company code must be unique within the company."})
        return super().validate(attrs)
