# serializers.py
from rest_framework import serializers
from placecode.models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"
