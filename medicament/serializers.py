from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Assistant




class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'



class UserSz(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = (
        "username", 
        "first_name", 
        "last_name", 
        "email" 
        )

class GetAssistantSerializer(serializers.ModelSerializer):
    user = UserSz()
    cabinet = serializers.SlugRelatedField(slug_field='name',read_only=True)
    class Meta : 
        model = Assistant
        fields = '__all__'