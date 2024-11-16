from django.db import models
from apps.catalogos.especie.models import Especie

class Animal(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=3, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=150)
    especie = models.ForeignKey(Especie, verbose_name= 'Especie', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Animales'

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'