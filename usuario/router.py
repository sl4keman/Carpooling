from django.urls import path
import usuario.views


urlpatterns = (
    path('registro_usuario', usuario.views.registro_usuario, name= 'registro_usuario'),
    path('iniciar_sesion', usuario.views.iniciar_sesion, name='iniciar_sesion'),
    path('editar_perfil', usuario.views.editar_perfil, name='editar_perfil'),
    path('eliminar_perfil', usuario.views.eliminar_perfil, name='eliminar_perfil'),
    path('cerrar_sesion', usuario.views.cerrar_sesion, name='cerrar_sesion'),
    )   