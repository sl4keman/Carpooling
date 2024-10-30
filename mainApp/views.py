from django.shortcuts import render
from viaje.models import Viaje


def index(request):
    return render(request, 'index.html')


def mostrar_mapa(request):
    return render(request, 'mapa.html')