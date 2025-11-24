from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import date
from django.utils import timezone

User = get_user_model()

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    sinopsis = models.TextField()
    fecha_publicacion = models.DateField(default=date.today, verbose_name="Fecha de Publicación")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='portadas/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} por {self.autor}"
    
class Resena(models.Model):
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE, related_name='reseñas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    PUNTUACION_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    puntuacion = models.IntegerField(
        choices=PUNTUACION_CHOICES,
        verbose_name="Puntuación"
    )
    texto = models.TextField(verbose_name="Contenido de la Reseña")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('libro', 'usuario')
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f'Reseña de {self.libro.titulo} por {self.usuario.username}'
    
class Anuncio(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-fecha']
