from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView, status 
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User,Group

# Create your views here.
from core.models import Appointment , Patient
from .serializers import AppointmentSerializer





class GetAppointmentView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        try:
            patient = Patient.objects.filter(cabinet=request.user.doctor.cabinet.id)
        except User.related_field.RelatedObjectDoesNotExist :
            patient = Patient.objects.filter(cabinet=request.user.assitant.cabinet.id)

        list_filter = patient.values_list('appointment',flat=True).distinct()
        appointment_data = Appointment.objects.filter(id__in=list_filter)
        serializer = AppointmentSerializer(appointment_data, many = True)
              
        return Response( serializer.data ,status=status.HTTP_200_OK) 



class AppointmentUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Appointment.objects.all()
    serializer_class =  AppointmentSerializer
    lookup_field = 'id'
    def retrieve(self, request,*args, **kwargs):
        instance = self.get_object()
        serializer =  AppointmentSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def perform_update(self, serializer):
        return serializer.save()
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial',False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)    
        instance = self.perform_update(serializer)
        serializer = AppointmentSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AppointmentDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Appointment.objects.all()
    serializer_class =  AppointmentSerializer
    lookup_field = 'id'