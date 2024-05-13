# serializers.py
from rest_framework import serializers
from placecode.models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

    def validate(self, attrs):
        country_code = attrs['country_code']
        if Country.objects.filter(country_code=country_code).exists():
            raise serializers.ValidationError({"country_code": "A country with this country code already exists"})
        return attrs
        
