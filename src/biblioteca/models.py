from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    categoria = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    descripcion = models.TextField(blank=True)
    puntuacion = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def __str__(self):
        return self.titulo
