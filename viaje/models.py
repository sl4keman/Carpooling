from django.db import models
from vehiculo.models import Vehiculo
from usuario.models import CustomUser


class Viaje(models.Model):
    direccion_origen = models.CharField(max_length=100, default='')
    direccion_destino = models.CharField(max_length=100, default='')
    hora_salida = models.TimeField()
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"{self.direccion_origen} -> {self.direccion_destino}"
    

class PasajeroViaje(models.Model):
    pasajero = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pasajero} // viaje:  {self.viaje}"