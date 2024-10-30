from django.db import models
from usuario.models import CustomUser

class Vehiculo(models.Model):
    linea = models.CharField(max_length=50, default='')
    marca = models.CharField(max_length=50, default='')
    TIPO_CHOICES = [
        ('Carro', 'Carro'),
        ('Moto', 'Moto'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='')
    asientos_disponibles = models.IntegerField()
    placa = models.CharField(max_length=10, default='')
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marca} {self.linea} ({self.placa}) - De: {self.usuario.nombre} {self.usuario.apellido} - {self.usuario.telefono}"
