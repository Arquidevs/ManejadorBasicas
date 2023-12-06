from django.db import models
from facturacion.models.Paciente import Paciente
from facturacion.models.Servicio import Servicio

###Tabla Estado de Cuenta
class EstadoCuenta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, default='Vacio')
    servicio = models.OneToOneField(Servicio, on_delete=models.CASCADE, default='Vacio')