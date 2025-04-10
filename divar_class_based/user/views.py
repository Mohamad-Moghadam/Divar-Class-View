from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from user.models import User
from user.serializerz import UserSerializer

class ListCreateView(ListCreateAPIView):
    queryset= User.objects.all()
    serializer_class= UserSerializer

class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset= User.objects.all()
    serializer_class= UserSerializer
