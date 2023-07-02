from django.shortcuts import render

#creamos un viewset
from rest_framework import viewsets
from api.serializers import ApiSerializer   

from personal.models import Persona

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class= ApiSerializer