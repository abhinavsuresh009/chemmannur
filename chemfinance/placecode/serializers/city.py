from placecode.models import Country, State, City
from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['country_code', 'state_code', 'city_code', 'city_name']

    # def validate(self, attrs):
    #     country_code = attrs['country_code']
    #     state_code = attrs['state_code']
    #     city_code = attrs['city_code']
    #     try:
    #         country = Country.objects.get(country_code=country_code)
    #     except Country.DoesNotExist:
    #         raise serializers.ValidationError({"country_code": "Country with this code does not exist."})
    #     try:
    #         state = State.objects.get(country=country, state_code=state_code)
    #     except State.DoesNotExist:
    #         raise serializers.ValidationError({"state_code": "State with this code does not exist in the provided country."})
    #     if City.objects.filter(state=state, city_code=city_code).exists():
    #         raise serializers.ValidationError({"city_code": "A city with this city code already exists in the provided state."})
    #     attrs['state'] = state
    #     return attrs

    # def create(self, validated_data):
    #     # Remove country_code and state_code
    #     city = City.objects.create(**validated_data)
    #     return city


