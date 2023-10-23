from rest_framework import serializers
from core.models import Cabinet


class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = '__all__'