from django.db import models
from enum import Enum

class Continentes(Enum):
    AFRICA = 'África'
    AMERICA = 'América'
    ASIA = 'Asia'
    EUROPA = 'Europa'
    OCEANIA = 'Oceanía'

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=80)
    fechaFundacion = models.DateField()
    tipoDeGobierno = models.CharField(max_length=100)
    poblacion = models.BigIntegerField()
    continente = models.CharField(max_length=20, choices=[(c.value, c.name) for c in Continentes])
    PIB = models.BigIntegerField()
    moneda = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.nombre}"
    

