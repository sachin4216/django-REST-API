# from django.shortcuts import render

from rest_framework import viewsets
from myapp.models import Hero
from myapp.serializer import heroSerializer

class heroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = heroSerializer
