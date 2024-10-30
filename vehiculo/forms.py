from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):  
    class Meta:
        model = Vehiculo
        fields = ['linea', 'marca', 'tipo', 'asientos_disponibles', 'placa', 'usuario']


class VehiculoEditForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['linea', 'marca', 'tipo', 'asientos_disponibles']
