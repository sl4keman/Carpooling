from django.contrib import admin
from .models import Viaje, PasajeroViaje

class PasajeroViajeInline(admin.TabularInline):
    model = PasajeroViaje

@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('direccion_origen', 'direccion_destino', 'hora_salida', 'vehiculo')
    search_fields = ('direccion_origen', 'direccion_destino')
    inlines = [
        PasajeroViajeInline,
    ]
