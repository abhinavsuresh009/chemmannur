from rest_framework import serializers 
from customer.models import Customer
# Serializer for Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        #fields = ['id', 'account_name', 'users', 'created']
        fields = "__all__"

# Serializer for Customer Search
class CustomerGetNameSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Customer
        fields = ['cusid', 'full_name','comcode','brcode']
        
    def get_full_name(request, obj):
        return f'{obj.fname} {obj.mname} {obj.lname}'
        #fields = "__all__"
