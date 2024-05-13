# serializers.py
from rest_framework import serializers
from placecode.models import State, Country

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['country_code', 'state_code', 'state_name']

  
    # def validate(self, attrs):
    #     print(attrs)
    #     country = attrs['country']
    #     state_code = attrs['state_code']
    #     if State.objects.filter(country=country, state_code=state_code).exists():
    #         raise serializers.ValidationError({"state_code" : "State code must be unique within the Country."})
    #     return super().validate(attrs)
    def validate(self, attrs):
        if self.context['request'].method == 'POST':
            country_code = attrs.get('country_code')
            state_code = attrs.get('state_code')

            if country_code:
                try:
                    country = Country.objects.get(country_code=country_code)
                except Country.DoesNotExist:
                    raise serializers.ValidationError({"country_code": "Country with this code does not exist."})
            else:
                country = None


            if state_code:
                if country:
                    # Only check state code uniqueness if creating a new instance
                    if State.objects.filter(country=country, state_code=state_code).exists():
                        raise serializers.ValidationError({"state_code": "A state with this state code already exists in the provided country."})
                else:
                    raise serializers.ValidationError({"state_code": "country is required to validate country code."})

            attrs['country'] = country
        return attrs

    def create(self, validated_data):
        return State.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        country_code = validated_data.get('country_code')
        state_code = validated_data.get('state_code')
        state_name = validated_data.get('state_name')

        # Check if state_code is provided and validate against existing state codes
        if state_code:
            try:
                country = Country.objects.get(country_code=country_code)
                existing_state = State.objects.exclude(pk=instance.pk).get(country=country, state_code=state_code)
                raise serializers.ValidationError("A state with this state code already exists in the provided country.")
            except (Country.DoesNotExist, State.DoesNotExist):
                pass  # No matching country or state found, which is okay for PATCH
        else:
            existing_state = None  # No state_code provided, no need for validation

        # Update the instance with validated data
        instance.country = country
        instance.state_code = state_code or instance.state_code
        instance.state_name = state_name or instance.state_name
            
        # Save the instance
        instance.save()

        return instance
