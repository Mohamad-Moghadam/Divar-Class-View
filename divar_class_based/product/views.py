from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from product.models import Product
from product.serializers import ProductSerializer


class ListCreateView(ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class= ProductSerializer