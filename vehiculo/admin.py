from django.contrib import admin
from .models import Vehiculo

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('linea', 'marca', 'tipo', 'asientos_disponibles', 'placa', 'usuario')
    search_fields = ('linea', 'marca', 'placa', 'usuario__nombre', 'usuario__apellido')
