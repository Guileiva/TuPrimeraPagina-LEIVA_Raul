from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import RegistroForm, PerfilUpdateForm
from django.urls import reverse_lazy

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('inicio')

    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

class RegistroUsuario(CreateView):
    form_class = RegistroForm
    template_name = 'registration/registro.html'
    success_url = reverse_lazy('login')

class ModificarPerfil(LoginRequiredMixin, UpdateView):
    model = get_user_model() 
    form_class = PerfilUpdateForm 
    template_name = 'appUsuarios/modificar_perfil.html'
    success_url = reverse_lazy('inicio') 

    def get_object(self):
        return self.request.user


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('inicio'))

