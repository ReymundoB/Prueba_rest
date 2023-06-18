from personal.models import Persona
from rest_framework import viewsets, permissions
from .serializers import ApiSerializer

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=ApiSerializer