from django.urls import path
import calificacion.views



urlpatterns = (
    path('hacer_calificacion/', calificacion.views.hacer_calificacion, name='hacer_calificacion'),
    path('hacer_calificacion/<int:viaje_id>/', calificacion.views.hacer_calificacion, name='hacer_calificacion'),
    ) 