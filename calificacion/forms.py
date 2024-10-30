from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = ['autor', 'valor_calificacion', 'comentario', 'pasajero_viaje']
