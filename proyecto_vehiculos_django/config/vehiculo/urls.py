from django.urls import path

from .views import index, listar, crear

urlpatterns = [
    path('', index, name='index'),
    path('lista_vehiculos/', listar, name= 'listar'),
    path('agregar_vehiculo/', crear, name= 'crear'),
    # path('crear_vehiculo/', crear, name= 'crear')
]
