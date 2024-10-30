from django.urls import path
import viaje.views



urlpatterns = (
    path('crear_viaje/', viaje.views.crear_viaje, name='crear_viaje'),
    path('buscar_viaje', viaje.views.buscar_viaje, name= 'buscar_viaje'),
    path('crear_viaje/<int:vehiculo_id>/', viaje.views.crear_viaje, name='crear_viaje'),
    path('eliminar_viaje', viaje.views.eliminar_viaje, name= 'eliminar_viaje'),
)  