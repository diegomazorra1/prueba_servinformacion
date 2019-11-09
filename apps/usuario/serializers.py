from django.db import models
from django_google_maps import fields as map_fields
from geoposition.fields import GeopositionField
from rest_framework import serializers
from .models import Usuarios
# Create your models here.


class UsuarioSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=15 )
    apellido = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=200)
    ciudad = serializers.CharField(max_length=11)
    geolocation = serializers.CharField (max_length=100)
    estadogeo= serializers.BooleanField(default=False)

class CreateUsuarioSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=15 )
    apellido = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=200)
    ciudad = serializers.CharField(max_length=11)
    geolocation = serializers.CharField (max_length=100)
    def create(self,data):
        return Usuarios.objects.create(**data)
        
