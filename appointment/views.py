from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView, status 
from rest_framework import generics
from rest_framework.response import Response

import datetime
from datetime import date

# Create your views here.
from core.models import Appointment , Patient,User
from .serializers import AppointmentSerializer



def get_date(datestr):
    datet = datetime.datetime.strptime(datestr,"%Y-%m-%d").date()
    return datet

class CreateAppointmentView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = AppointmentSerializer
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AppointmentSerializer
        else:
            return AppointmentSerializer
    

    def create(self, request, *args, **kwargs):
        data = self.request.data.copy()
        dat = data['date']
        try:
            patient = Patient.objects.filter(cabinet=request.user.doctor.cabinet.id)
        except User.related_field.RelatedObjectDoesNotExist : 
            patient = Patient.objects.filter(cabinet=request.user.assistant.cabinet.id) 
        
        list_filter = patient.values_list('appointment',flat=True).distinct()
        appoint = Appointment.objects.filter(id__in=list_filter).filter(date=dat)
        check = False
        print("hadi 9bel " ,type(dat),dat)
        print("hadi menbe3de",type(get_date(dat)),get_date(dat))
        print(date.today())
        if date.today() <= get_date(dat):
            for app in appoint:
                if  datetime.datetime.strptime(data['fm'],"%H:%M").time()  >= app.fm and  datetime.datetime.strptime(data['fm'],"%H:%M").time() < app.To:
                    check = True
                    content = {"message":f"Cet  heur {data['fm']} est déjà  réservé, veuillez choisir un autre heure"}
                    return Response( content , status=status.HTTP_201_CREATED)
                if  datetime.datetime.strptime(data['To'],"%H:%M").time() >  app.fm and  datetime.datetime.strptime(data['To'],"%H:%M").time()<=  app.To:
                    check = True
                    content = {"message":f"Cet heur {data['To']} est déjà  réservé,veuillez choisir un autre heure "}
                    return Response( content , status=status.HTTP_201_CREATED)
                if  app.fm >=  datetime.datetime.strptime(data['fm'],"%H:%M").time() and  app.fm <  datetime.datetime.strptime(data['To'],"%H:%M").time():
                    check = True
                    content = {"message":"ce rendez-vous a un rendez-vous entre eux, veuillez choisir un autre rendez-vous"}
                    return Response( content , status=status.HTTP_201_CREATED)
        else:
            content = {"message":f"ce jour {data['date']}  est  déjà passé, veuillez choisir un autre jour"}
            return Response( content , status=status.HTTP_201_CREATED)
        if not check:
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED,headers = headers)







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



class UpdateAppointmentView(generics.RetrieveUpdateAPIView):
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

class DeleteAppointmentView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Appointment.objects.all()
    serializer_class =  AppointmentSerializer
    lookup_field = 'id'