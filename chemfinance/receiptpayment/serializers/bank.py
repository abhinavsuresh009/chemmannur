from rest_framework import serializers
from receiptpayment.models import BankEntry
from django.core.validators import RegexValidator

# def validate_name(value):

#     if not value.isalpha() or value.startswith(' ') or value.endswith(' '):
#         raise serializers.ValidationError("You can not use numbers for names")
validate_name = RegexValidator(
    regex='^[^\s].+[a-zA-Z]+[a-zA-Z]+$',
    message='Name must contain only alphabetic characters and cannot start or end with spaces.',
    code='invalid_name'
)

class BankSerializer(serializers.ModelSerializer):
    party_name = serializers.CharField(max_length=100, validators=[validate_name])
    bank_name = serializers.CharField(max_length=100, validators=[validate_name])


    class Meta:
        model = BankEntry
        fields = '__all__'

   