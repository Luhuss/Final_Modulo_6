from django.contrib import admin
from .models import Vehiculo

# Register your models here.
# https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin
class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'condicion_de_precio')
    
    def condicion_de_precio(self, obj):
        if obj.valoracion < 10000:
            return 'Bajo'
        elif 10000 <= obj.valoracion <= 30000:
            return 'Medio'
        else:
            return 'Alto'
admin.site.register(Vehiculo, VehiculoAdmin)
