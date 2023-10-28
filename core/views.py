from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView, status 
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import Group



from .serializers import  UserSerializer
# Create your views here.


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        groups_list = user.groups.all().values_list('name',flat =True).distinct()
        # Add custom claims
        token['name'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['active'] = user.is_active
        try:
            token['groups'] = groups_list[0]
        except IndexError:
            token['groups'] = None
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



class AllUsersView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class GetUserView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = User.objects.get(pk=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data , status=status.HTTP_200_OK)