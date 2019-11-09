from django.db import models
from django_google_maps import fields as map_fields
from geoposition.fields import GeopositionField
# Create your models here.



class Usuarios(models.Model):


    nombre = models.CharField(max_length=15 )
    apellido = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=11)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    estadogeo= models.BooleanField(default=False)

    def save(self,*args, **kwargs):
        self.estadogeo=True
        return super(Usuarios, self).save( *args, **kwargs)
