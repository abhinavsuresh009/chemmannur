from rest_framework import serializers
from companybranch.models import Branch
from rest_framework.exceptions import ValidationError


# serializer for Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
        
    def validate(self, attrs):
        print(attrs)
        company = attrs['company']
        brcode = attrs['brcode']
        if Branch.objects.filter(company=company, brcode=brcode).exists():
            raise serializers.ValidationError({"brcode" : "Branch code must be unique within the company."})
        return super().validate(attrs)
       
