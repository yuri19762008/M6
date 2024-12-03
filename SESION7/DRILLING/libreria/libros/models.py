

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Book(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    valoracion = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10000)]
    )

    def __str__(self):
        return self.titulo