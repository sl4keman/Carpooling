from django.contrib import admin
from .models import Calificacion

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('autor', 'valor_calificacion', 'comentario', 'pasajero_viaje')