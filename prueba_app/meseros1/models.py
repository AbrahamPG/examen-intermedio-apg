from django.db import models


# Create your models here.
class Meseros1(models.Model):
    nombre = models.CharField(max_length=25)
    pais = models.CharField(max_length=25)
    edad = models.IntegerField()
    dni = models.CharField(max_length=9, default='00000000')
