from django.db import models

class NivelRuta(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=5, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=100)
    class Meta:
        verbose_name_plural = 'Niveles de Ruta'

    def __str__(self):
        return f'{self.codigo} - {self.descripcion}'
