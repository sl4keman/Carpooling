from django import forms
from .models import Viaje

class ViajeForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['direccion_origen', 'direccion_destino', 'hora_salida', 'vehiculo']


class ViajeEditForm(forms.ModelForm):
    class Meta:
        model = Viaje
        fields = ['direccion_origen', 'direccion_destino', 'hora_salida', 'vehiculo']
