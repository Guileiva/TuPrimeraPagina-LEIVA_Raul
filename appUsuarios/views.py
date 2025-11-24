from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import RegistroForm, PerfilUpdateForm, AvatarForm
from .models import Avatar
from django.urls import reverse_lazy

class RegistroUsuario(CreateView):
    form_class = RegistroForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

class ModificarPerfil(LoginRequiredMixin, UpdateView):
    model = get_user_model() 
    form_class = PerfilUpdateForm 
    template_name = 'appUsuarios/modificar_perfil.html'
    success_url = reverse_lazy('lista_libros') 

    def get_object(self):
        return self.request.user


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('inicio'))

