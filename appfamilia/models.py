from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    lista = models.CharField(max_length=30)