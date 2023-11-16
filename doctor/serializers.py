from rest_framework import serializers
from core.models import Doctor,Specialite
from core.models import User
from cabinet.serializers import CabinetSerializer
from rest_framework.validators import UniqueValidator




class SpecialiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialite
        fields = '__all__'





class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk' , 'username', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }


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

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Doctor
        fields = '__all__'


class UserDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
        "id", 
        "username", 
        "first_name", 
        "last_name", 
        "email", 
        "role",)
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    class Meta:
        model = User
        fields = '__all__'

class GetDoctorSerialzer(serializers.ModelSerializer):
    user = UserDoctorSerializer(required=True, many=False)
    specialiste = SpecialiteSerializer(required=True, many=False)
    cabinet = CabinetSerializer(required=True, many=False)
    class Meta:
        model = Doctor
        fields = '__all__'  
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data.pop('password2')
        create_user =  User.objects.create(**user_data)
        create_doctor = Doctor.objects.create(user=create_user,**validated_data)
        return create_doctor
    
class UpdateDoctorSerializer(serializers.ModelSerializer):
    user = UpdateUserSerializer()
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('phone', )
    
    def update(self, instance, validated_data):
        user_serializer = self.fields['user']
        user_instance = instance.user
        user_data = validated_data.pop('user')
        user_serializer.update(user_instance,user_data)
        instance = super().update(instance, validated_data)
        return instance