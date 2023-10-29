from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView, status 
from rest_framework import generics
from rest_framework.response import Response

from django.contrib.auth.models import Group


from core.models import Doctor, Specialite , Cabinet , User
from .serializers import DoctorSerializer, GetDoctorSerialzer, UpdateDoctorSerializer,  UserSerializer


# Create your views here.

class CreateDoctorView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DoctorSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        user = User.objects.create_user(data['username'], password=data['password'])
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.is_superuser = False
        user.is_staff = False
        user.email = data['email']
        gr = Group.objects.get(name='doctor')
        user.groups.add(gr) 
        user.save()
        last_user = User.objects.last()
        get_specialite = Specialite.objects.get(pk=data['specialite'])
        cabinet = Cabinet.objects.get(pk=data['cabinet'])
        create_doctor  = Doctor.objects.create(
            user= last_user,
            cabinet = cabinet,
            inp = data['inp'],
            gender=data['gender'],
            phone= data['phone'],
            address = data['address'],
            specialiste = get_specialite,

        )
        last_doctor = Doctor.objects.last()
        user_serializer =UserSerializer(last_user)
        doctor_serializer = DoctorSerializer(last_doctor)
        content = {'message':"votre compte a été créé !!"}
        return Response(content, status=status.HTTP_201_CREATED)
    


class GetDoctorView(APIView):

    #permission_classes = (IsAuthenticated,)
    def get(self, request):
        doctor = Doctor.objects.all()
        serializer = GetDoctorSerialzer(doctor,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)


class UpdateDoctorView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Doctor.objects.all()
    serializer_class = UpdateDoctorSerializer
    lookup_field = 'id'

class DeleteDoctorView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'id'