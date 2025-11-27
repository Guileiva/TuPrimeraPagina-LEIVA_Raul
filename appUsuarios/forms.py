from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Avatar

class RegistroForm(UserCreationForm):
    imagen = forms.ImageField(required=False, label="Avatar (Opcional)")
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )
        help_texts = {'username': ""}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()            
            imagen = self.cleaned_data.get('imagen')

            if imagen:
                Avatar.objects.create(user=user, imagen=imagen)
            return user

class PerfilUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True) 
    imagen = forms.ImageField(required=False, label="Avatar (Opcional)")
    class Meta:
        model = User
        
        fields = ('first_name', 'last_name', 'email',) 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def save(self, commit=True):        
        user = super().save(commit=False)
        
        if commit:
            user.save()                        
            imagen = self.cleaned_data.get('imagen')

            if imagen:
                Avatar.objects.update_or_create(user=user, defaults={'imagen': imagen})
            return user

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

        