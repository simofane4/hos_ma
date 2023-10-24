from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView, status 
from rest_framework import generics
from rest_framework.response import Response


from core.models import Cabinet
from .serializers import CabinetSerializer


# Create your views here.

class CreateCabinetView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CabinetSerializer
    
    
class GetCabinetView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        cabinet = Cabinet.objects.all()
        serializer = CabinetSerializer(cabinet,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateCabinetView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
    lookup_field = 'id'
    def retrieve(self, request,*args, **kwargs):
        instance = self.get_object()
        serializer = CabinetSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def perform_update(self, serializer):
        return serializer.save()
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial',False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)    
        instance = self.perform_update(serializer)
        serializer = CabinetSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteCabinetView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
    lookup_field = 'id'