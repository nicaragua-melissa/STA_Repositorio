from django.db import models

class Departamento(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=3, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    class Meta:
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return f'{self.codigo} - {self.descripcion}'
# Create your models here.
