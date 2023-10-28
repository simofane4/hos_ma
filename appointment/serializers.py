from rest_framework import serializers
from core.models import User
from core.models import Appointment




class AppointmentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Appointment
        fields = '__all__'