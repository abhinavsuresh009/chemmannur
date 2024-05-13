from placecode.models import Country, State, City
from rest_framework import serializers

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['country_code', 'state_code', 'city_code', 'city_name']

    
    def validate(self, attrs):
        if self.context['request'].method == 'POST':
            country_code = attrs.get('country_code')
            state_code = attrs.get('state_code')
            city_code = attrs.get('city_code')

            if country_code:
                try:
                    country = Country.objects.get(country_code=country_code)
                except Country.DoesNotExist:
                    raise serializers.ValidationError({"country_code": "Country with this code does not exist."})
            else:
                country = None

            if state_code:
                try:
                    if country:
                        state = State.objects.get(country=country, state_code=state_code)
                    else:
                        raise serializers.ValidationError({"state_code": "Country code is required to validate state code."})
                except State.DoesNotExist:
                    raise serializers.ValidationError({"state_code": "State with this code does not exist in the provided country."})
            else:
                state = None

            if city_code:
                if state:
                    # Only check city code uniqueness if creating a new instance
                    if City.objects.filter(state=state, city_code=city_code).exists():
                        raise serializers.ValidationError({"city_code": "A city with this city code already exists in the provided state."})
                else:
                    raise serializers.ValidationError({"city_code": "State code is required to validate city code."})

            attrs['state'] = state
        return attrs

    def create(self, validated_data):
        return City.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        country_code = validated_data.get('country_code')
        state_code = validated_data.get('state_code')
        city_code = validated_data.get('city_code')
        city_name = validated_data.get('city_name')

        # Check if city_code is provided and validate against existing city codes
        if city_code:
            try:
                country = Country.objects.get(country_code=country_code)
                state = State.objects.get(country=country, state_code=state_code)
                existing_city = City.objects.exclude(pk=instance.pk).get(state=state, city_code=city_code)
                raise serializers.ValidationError("A city with this city code already exists in the provided state.")
            except (Country.DoesNotExist, State.DoesNotExist, City.DoesNotExist):
                pass  # No matching country, state, or city found, which is okay for PATCH
        else:
            existing_city = None  # No city_code provided, no need for validation

        # Update the instance with validated data
        instance.country_code = country_code or instance.country_code
        instance.state_code = state_code or instance.state_code
        instance.city_code = city_code or instance.city_code
        instance.city_name = city_name or instance.city_name
        
        # Save the instance
        instance.save()

        return instance