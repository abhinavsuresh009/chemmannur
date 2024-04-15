from rest_framework import serializers 
from customer.models import Customer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        #fields = ['id', 'account_name', 'users', 'created']
        fields = "__all__"

class CustomerGetNameSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Customer
        fields = ['cusid', 'full_name']
        
    def get_full_name(request, obj):
        return f'{obj.fname} {obj.mname} {obj.lname}'
        #fields = "__all__"
