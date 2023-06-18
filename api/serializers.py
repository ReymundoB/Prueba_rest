from rest_framework import serializers
from personal.models import Persona


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields='__all__'
