from rest_framework import serializers 
from customer.models import *
from companybranch.models import *
# Serializer for Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        #fields = ['id', 'account_name', 'users', 'created']
        fields = "__all__"
        
    def validate(self, attrs):
        # giving conditions to username
        brcode = attrs['brcode']
        comcode = attrs['comcode']
        if not Company.objects.filter(comcode=comcode).exists():
            raise serializers.ValidationError({"comcode": "Company code does not exist."})
        if not Branch.objects.filter(company=comcode, brcode=brcode).exists():
            raise serializers.ValidationError({"brcode" : "Branch code is not within the company."})

        return attrs


# Serializer for Customer Search
class CustomerGetNameSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Customer
        fields = ['id', 'cusid', 'full_name','comcode','brcode','address1', 'address2','phone','trdate','mob','aadhaar']
        
    def get_full_name(request, obj):
        return f'{obj.fname} {obj.mname} {obj.lname}'
        #fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'