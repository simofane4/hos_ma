from rest_framework import serializers
from core.models import User
from core.models import Medicament




class MedicamentSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Medicament
        fields = '__all__'