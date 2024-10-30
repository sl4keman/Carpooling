from django.urls import path
import vehiculo.views


urlpatterns = (
    path('registrar_vehiculo', vehiculo.views.registrar_vehiculo, name= 'registrar_vehiculo'),
    path('listar_vehiculos/', vehiculo.views.listar_vehiculos, name='listar_vehiculos'),
    path('eliminar_vehiculo', vehiculo.views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('editar_vehiculo', vehiculo.views.editar_vehiculo, name='editar_vehiculo'),
) 