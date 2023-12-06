from django.db import models
from facturacion.models.Contrato import Contrato

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    id = models.CharField(max_length=10, primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    tipo_id = models.CharField(max_length=40, choices=[('cedula', 'Cedula'), 
                                                       ('cedula extranjeria', 'Cedula Extranjeria'),
                                                       ('pasaporte', 'Pasaporte'),
                                                       ('tarjeta de identidad', 'Tarjeta de Identidad' ),
                                                       ('registro vicil', 'Registro Civil')])
    id_contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
