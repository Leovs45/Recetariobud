from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    costo_g = models.DecimalField(max_digits=6, decimal_places=4)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    notas = models.TextField(blank=True, null=True)  # Puede estar vacío

    def __str__(self):
        return self.nombre

class RecetaIngrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    porcentaje_panadero = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad_gramos = models.DecimalField(max_digits=6, decimal_places=2)
    

    class Meta:
        unique_together = ("receta", "ingrediente")  # Evita duplicados

    def __str__(self):
        return f"{self.cantidad_gramos}g de {self.ingrediente.nombre} en {self.receta.nombre}"    