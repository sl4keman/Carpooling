from django.shortcuts import render, redirect
from .forms import CalificacionForm


def hacer_calificacion(request, viaje_id=None):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            calificacion = form.save()
            return redirect('index')
    else:
        form = CalificacionForm()
    return render(request, 'hacer_calificacion.html', {'form': form})
