from django.db import models
from viaje.models import PasajeroViaje


class Calificacion(models.Model):
    AUTOR_CHOICES = [
        ('Conductor', 'Conductor'),
        ('Pasajero', 'Pasajero'),
    ]
    VALOR_CALIFICACION_CHOICES = [
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    autor = models.CharField(max_length=10, choices=AUTOR_CHOICES, default='Pasajero')
    valor_calificacion = models.PositiveSmallIntegerField(choices=VALOR_CALIFICACION_CHOICES, default=0)
    comentario = models.TextField(max_length = 300, default='')
    pasajero_viaje = models.ForeignKey(PasajeroViaje, on_delete=models.CASCADE)

    def __str__(self):
        if self.autor == 'Pasajero':
            return f"Calificación de {self.pasajero_viaje.pasajero.nombre} - Valor: {self.valor_calificacion}"
        elif self.autor == 'Conductor':
            return f"Calificación de {self.pasajero_viaje.viaje.vehiculo.usuario.nombre} - Valor: {self.valor_calificacion}"