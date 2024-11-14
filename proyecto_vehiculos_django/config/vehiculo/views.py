from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Vehiculo
from .forms import VehiculoForm

# Create your views here.

# views o controller para página inicial 
def index(request):
    return render(request, 'index.html')

def condicion_de_precio(obj):
        if obj.precio < 10000:
            return 'Bajo'
        elif 10000 <= obj.precio <= 30000:
            return 'Medio'
        else:
            return 'Alto'

# views o controller para listar los vehiculos
def listar(request):
    vehiculos = Vehiculo.objects.all()
    vehiculos_condicion = []
    for i in vehiculos:
        condicion = condicion_de_precio(i)
        i.condicion_precio = condicion
        vehiculos_condicion.append(i)
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos_condicion})

# Vista para crear un vehículo
def crear(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehículo creado correctamente')
            return redirect('listar')
        else:
            messages.error(request, 'Error en el formulario. Por favor, corrige los errores.')
    else:
        form = VehiculoForm()
    return render(request, 'agregar_vehiculos.html', {'form': form})