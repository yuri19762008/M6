from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    num_paginas = models.IntegerField()
    imagen = models.URLField()

    class Meta:
        db_table = 'libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo