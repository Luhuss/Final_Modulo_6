from django import forms 
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
        widgets = {
            'marca': forms.Select(
                attrs={
                    'class': 'form-control',
                    'requieder': True
                }
            ),
            'modelo': forms.TimeInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Corola',
                    'requiered': True
                }
            ),
            'serial_carroceria': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'D1234567890',
                    'requiered': True
                }
            ),
            'serial_motor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'D1234567890',
                    'requiered': True
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'requiered': True
                }
            )
        }