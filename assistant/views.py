from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView, status 
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User,Group




from core.models import Cabinet,Assistant
from .serializers import AssistantSerializer , GetAssistantSerializer

# Create your views here.

class CreateAssistantView(generics.ListCreateAPIView):
    permission_classes =  (IsAuthenticated,)
    serializer_class = AssistantSerializer
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        user = User.objects.create_user(data['username'], password=data['password'])
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.is_superuser = False
        user.is_staff = False
        user.email = data['email']
        gr = Group.objects.get(name = 'assistant')
        user.groups.add(gr) 
        user.save()
        last_user = User.objects.last()
        cabinet = Cabinet.objects.get(pk=data['cabinet'])
        create_doctor  = Assistant.objects.create(
            user= last_user,
            cabinet = cabinet,
            img = data['img'],
            cin = data['cin'],
            gender=data['gender'],
            phone= data['phone'],
            address = data['address'],
        )
    
        content = {'message':"votre compte a été créé !!"}
        return Response(content, status=status.HTTP_201_CREATED)

class AssistantGetView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        assistant = Assistant.objects.all()
        serializer = GetAssistantSerializer(assistant,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class AssistantUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class  = AssistantSerializer
    ookup_field = 'id'
    def retrieve(self, request,*args, **kwargs):
        instance = self.get_object()
        serializer =  AssistantSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial',False)
        instance = self.get_object()
        serializer = AssistantSerializer(instance,data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)    
        serializer.save()
        serializer = AssistantSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)



class AssistantDeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer
    lookup_field = 'id'
