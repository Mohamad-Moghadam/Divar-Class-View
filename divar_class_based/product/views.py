from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from product.models import Product
from product.serializers import ProductSerializer


class ListCreateView(ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer

class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer