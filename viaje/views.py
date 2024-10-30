from django.shortcuts import render, redirect, get_object_or_404
from .forms import ViajeForm, ViajeEditForm
from .models import Viaje, Vehiculo, PasajeroViaje
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def crear_viaje(request, vehiculo_id=None):
    if request.method == 'POST':
        form = ViajeForm(request.POST)
        if form.is_valid():
            viaje = form.save(commit=False)
            if vehiculo_id:
                vehiculo = Vehiculo.objects.get(id=vehiculo_id)
                viaje.vehiculo = vehiculo
            viaje.save()
            return redirect('index') 
    else:
        form = ViajeForm()
    return render(request, 'crear_viaje.html', {'form': form})

 
def buscar_viaje(request):
    viajes = Viaje.objects.all()
    if request.method == 'POST':
        viaje_id = request.POST.get('viaje_id')
        if viaje_id:
            viaje = Viaje.objects.get(id=viaje_id)
            user = request.user

            if viaje.vehiculo.asientos_disponibles > 0:
                pasajero_viaje = PasajeroViaje.objects.create(pasajero=user, viaje=viaje)
                viaje.vehiculo.asientos_disponibles -= 1
                viaje.vehiculo.save()
                messages.success(request, '¡Reserva realizada con éxito!')
            else:
                messages.error(request, 'No hay asientos disponibles.')
            return redirect('buscar_viaje')
        else:
            messages.error(request, 'Error al procesar la reserva.')
    return render(request, 'buscar_viaje.html', {'viajes': viajes})


def eliminar_viaje(request):
    if request.method == 'POST':
        placa_vehiculo = request.POST.get('placa_vehiculo')
        viaje = Viaje.objects.filter(vehiculo__placa=placa_vehiculo).first()
        if viaje:
            viaje.delete()
            return redirect('index')  
        else:
            
            return render(request, 'eliminar_viaje.html', {'error_message': 'No se encontró ningún viaje con esa placa.'})
    else:
        return render(request, 'eliminar_viaje.html')