from django.db import models


class Especie(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=5, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=150)

    class Meta:
        verbose_name_plural = 'Especies'

    def __str__(self):
        return f'{self.codigo} - {self.descripcion}'