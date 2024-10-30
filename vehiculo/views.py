from django.shortcuts import render, redirect
from .forms import VehiculoForm, VehiculoEditForm
from .models import Vehiculo
from django.contrib import messages


def registrar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save()
            return redirect('crear_viaje', vehiculo_id=vehiculo.id)  
    else:
        form = VehiculoForm()
    return render(request, 'registrar_vehiculo.html', {'form': form})


def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'listar_vehiculos.html', {'vehiculos': vehiculos})


def eliminar_vehiculo(request):
    if request.method == 'POST':
        placa_vehiculo = request.POST.get('placa_vehiculo')
        vehiculo = Vehiculo.objects.filter(placa=placa_vehiculo, usuario=request.user).first()
        if vehiculo:
            vehiculo.delete()
            return redirect('listar_vehiculos')  
        else:
            return render(request, 'eliminar_vehiculo.html', {'error_message': 'No se encontró ningún vehículo con esa placa o no tienes permiso para eliminarlo.'})
    return render(request, 'eliminar_vehiculo.html')


def editar_vehiculo(request):
    vehiculo = None
    form = None

    if request.method == 'POST':
        # Recuperar el vehículo de la sesión
        vehiculo_id = request.session.get('vehiculo_id')
        if vehiculo_id:
            vehiculo = Vehiculo.objects.filter(id=vehiculo_id, usuario=request.user).first()
            if vehiculo:
                form = VehiculoEditForm(request.POST, instance=vehiculo)
                if form.is_valid():
                    form.save()
                    # Eliminar el vehículo de la sesión después de guardar
                    del request.session['vehiculo_id']
                    return redirect('listar_vehiculos')
            else:
                error_message = 'No se encontró ningún vehículo con esa placa o no tienes permiso para editarlo.'
                return render(request, 'editar_vehiculo.html', {'error_message': error_message})
        else:
            error_message = 'No se encontró ningún vehículo en la sesión.'
            return render(request, 'editar_vehiculo.html', {'error_message': error_message})

    elif request.method == 'GET' and 'placa_vehiculo' in request.GET:
        placa_vehiculo = request.GET.get('placa_vehiculo')
        vehiculo = Vehiculo.objects.filter(placa=placa_vehiculo, usuario=request.user).first()
        if vehiculo:
            form = VehiculoEditForm(instance=vehiculo)
            # Guardar el vehículo en la sesión
            request.session['vehiculo_id'] = vehiculo.id
        else:
            error_message = 'No se encontró ningún vehículo con esa placa o no tienes permiso para editarlo.'
            return render(request, 'editar_vehiculo.html', {'error_message': error_message})

    return render(request, 'editar_vehiculo.html', {'form': form})
