from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, status 
from rest_framework import generics
from rest_framework.response import Response
from core.models import User


from core.models import Ordonnance
from .serializers import OrdonnanceSerializer
# Create your views here.

class CreateOrdonnanceView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrdonnanceSerializer
        else:
            return OrdonnanceSerializer

    def create(self, request, *args, **kwargs):
        # Copy parsed content from HTTP request
        data = request.data.copy()
        # Add id cabinet  of currently logged user
        data['cabinet'] = request.user.doctor.cabinet.id
        # Default behavior but pass our modified data instead
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class GetOrdonnanceView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        ordonnacne_data = Ordonnance.objects.filter(cabinet=request.user.doctor.cabinet.id)

        serializer = OrdonnanceSerializer(ordonnacne_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class UpdateOrdonnanceView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ordonnance.objects.all()
    serializer_class =  OrdonnanceSerializer
    lookup_field = 'id'
    def retrieve(self, request,*args, **kwargs):
        instance = self.get_object()
        serializer =  OrdonnanceSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial',False)
        instance = self.get_object()
        data = request.data.copy()
        # Add id of currently logged user
        try:
            data['cabinet'] = request.user.doctor.cabinet.id
        except User.related_field.RelatedObjectDoesNotExist : 
            data['cabinet'] = request.user.assistant.cabinet.id
        # Default behavior but pass our modified data instead
        serializer = self.get_serializer(instance,data=data, partial=partial)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteOrdonnanceView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Ordonnance.objects.all()
    serializer_class =  OrdonnanceSerializer
    lookup_field = 'id'