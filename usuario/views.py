from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, ProfileEditForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout


def registro_usuario(request):
    if request.method == 'POST':
        print("Formulario POST recibido")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Usuario registrado exitosamente")
            return redirect('iniciar_sesion')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro_usuario.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'iniciar_sesion.html', {'form': form})


def editar_perfil(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileEditForm(instance=user)
    return render(request, 'editar_perfil.html', {'form': form})


def eliminar_perfil(request):
    if request.method == 'POST':

        usuario = request.user
        usuario.delete()
        logout(request)

        return redirect('index')  
    else:
        return render(request, 'eliminar_perfil.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('index')