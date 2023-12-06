from django.db import models
from facturacion.models.Servicio import Servicio
from facturacion.models.Contrato import Contrato
    

###Tabla Manual Tarifario
class Manual_Tarifario(models.Model):
    id_servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    id_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    precio = models.IntegerField()