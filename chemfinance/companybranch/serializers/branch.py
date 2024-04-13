from rest_framework import serializers
from companybranch.models import Branch


# serializer for Branch

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


    def to_representation(self, instance):
        comcode = self.context.get('comcode')
        if comcode and instance.company.comcode != comcode:
            return None
        return super().to_representation(instance)