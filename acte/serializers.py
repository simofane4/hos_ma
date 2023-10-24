from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import ActeDemander,ActeFait




class ActeDemanderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActeDemander
        fields = '__all__'
        
class ActeFaitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActeFait
        fields = '__all__'