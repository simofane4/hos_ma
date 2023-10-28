from rest_framework import serializers
from core.models import User
from core.models import Ordonnance





class OrdonnanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordonnance
        fields = '__all__'
