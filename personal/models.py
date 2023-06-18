from typing import Type
from django.db import models
from django.db.models.options import Options

# Create your models here.
class Persona(models.Model):
    Nombre = models.CharField(max_length=30, blank=False, null=False )
    Apellido_paterno=models.CharField(max_length=30, blank=False, null=False)
    Apellido_materno=models.CharField(max_length=30,blank=False, null=False)
    Hobbie= models.CharField(max_length=60, blank=True, null=True)
    Documento=models.CharField(max_length=60, blank=True, null=True)
    Tipo_documento=models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.Nombre + ' '+self.Apellido_paterno +' '+self.Hobbie
