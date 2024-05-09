from rest_framework import serializers
from .models import GoldRate
from companybranch.models import Company, Branch

class GoldrateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoldRate
        fields = '__all__'
        
    def validate(self, attrs):
        brcode = attrs['brcode']
        comcode = attrs['comcode']
        if not Company.objects.filter(comcode=comcode).exists():
            raise serializers.ValidationError({"comcode": "Company code does not exist."})
        if not Branch.objects.filter(brcode = brcode).exists():
            raise serializers.ValidationError({"brcode": "Branch code does not exist."})
        return attrs
    
    
        
