from rest_framework import serializers
from core.models import User






class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = (
        "id", 
        "last_login",
        "username", 
        "first_name", 
        "last_name", 
        "email", 
        "groups",)