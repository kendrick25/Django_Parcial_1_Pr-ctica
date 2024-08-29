from django.db import models

class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField()

    def __str__(self):
        return self.titulo
