from django.db import models

# Create your models here.

class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    cuerpo = models.TextField()
    publicado = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_publicacion"]

    def __str__(self):
        return self.titulo
