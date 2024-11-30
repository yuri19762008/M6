from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'isbn', 'num_paginas', 'imagen']
        widgets = {
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'num_paginas': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.URLInput(attrs={'class': 'form-control'}),
        }