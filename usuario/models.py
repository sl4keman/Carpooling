from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=50, default='')
    apellido = models.CharField(max_length=50, default='')
    dni = models.CharField(max_length=10, default='')
    telefono = models.CharField(max_length=10, default='') 
    email = models.EmailField(unique=True, default='')
    TIPO_CHOICES = [
        ('Conductor', 'Conductor'),
        ('Pasajero', 'Pasajero'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='')

    # Añadir related_name único para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions'
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Teléfono: {self.telefono}"
