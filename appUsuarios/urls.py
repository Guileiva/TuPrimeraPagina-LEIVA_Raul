from django.urls import path
from appUsuarios.views import login_view, logout_view, RegistroUsuario, ModificarPerfil
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/', login_view, name='login'), 
    path('registro/', RegistroUsuario.as_view(), name='registro'), 
    path('logout/', logout_view, name='logout'), 
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/cambiar_password.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/cambiar_password_exito.html'), name='password_change_done'),
    path('perfil/modificar/', ModificarPerfil.as_view(), name='modificar_perfil'),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
