#### crear carpeta para almacenar el proyecto
mkdir config
mkdir nombre_carpeta

### ingresar a la carpeta creada
cd config
cd nombre_carpeta

### crear entorno virtual django_development
python3 -m venv .venv


### abrir el entorno virtual
source .venv/bin/activate


### instalar django en el entorno virtual
pip install --upgrade pip /*actualiza el pip */
pip install django /* instala django */
pip list /* para verificar los programas instalados */


### crear un proyecto django
django-admin startproject nombre_proyecto
django-admin startproject config

### ubicarse en la carpeta creada
cd vehiculo

### crear la app
django-admin startapp vehiculo /* nombre del archivo creado en setings.py */

### modificar el archivo settings.py para registrar el aplicativo o app creada en el punto 6, creado con django-admin startapp 
INSTALLED_APPS = [
    'vehiculo.apps.VehiculoConfig',
]

### ejecutar migraciones
    python manage.py migrate

### ejecutar el servidor local para verificar que todo este correcto
python manage.py runserver

/* esto se hace en la carpeta urls.py 
path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('', include('book.urls')),
*/

### crear archivo urls.py dentro de la carpeta del programa en este caso (book_2)
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
]

#### dentro de la carpeta views.py escribir lo siguiente:
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bienvenido al sitio de libros")

#### crear carpeta template
book/template