from rest_framework import serializers
from companybranch.models import Branch
from rest_framework.exceptions import ValidationError


# serializer for Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
       
    def create(self, validated_data):
        company = validated_data.get('company')
        brcode = validated_data.get('brcode')
        
        # Check if the brcode is unique within the company
        if Branch.objects.filter(company=company, brcode=brcode).exists():
            raise serializers.ValidationError({"Company" : "Branch code must be unique within the company."})
        
        return super().create(validated_data)