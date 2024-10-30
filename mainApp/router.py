from django.urls import path
import mainApp.views

urlpatterns = (
    path('', mainApp.views.index, name='index'),
    path('mapa/', mainApp.views.mostrar_mapa, name='mapa'),
    )