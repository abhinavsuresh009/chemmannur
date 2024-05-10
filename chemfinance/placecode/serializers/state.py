# serializers.py
from rest_framework import serializers
from placecode.models import State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"

  
    def validate(self, attrs):
        print(attrs)
        country = attrs['country']
        state_code = attrs['state_code']
        if State.objects.filter(country=country, state_code=state_code).exists():
            raise serializers.ValidationError({"state_code" : "State code must be unique within the Country."})
        return super().validate(attrs)
