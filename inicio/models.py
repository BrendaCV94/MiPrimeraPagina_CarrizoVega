from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    año = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(datetime.date.today().year)
        ]
    )
    imagen = models.ImageField(upload_to='libros', null=True, blank=True) 

    def __str__(self):
        return f"{self.titulo} - {self.autor} ({self.año})"

