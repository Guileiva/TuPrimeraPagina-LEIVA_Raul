from django import forms
from .models import Libro, Resena
from datetime import date 

class LibroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if not self.instance.pk:
            self.initial['fecha_publicacion'] = date.today().strftime('%Y-%m-%d')

    class Meta:
        model = Libro 
        fields = ['titulo', 'autor', 'sinopsis', 'imagen']

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['puntuacion', 'texto'] 
        
        widgets = {
            'texto': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe aquí tu opinión sobre el libro...'}),
        
        }