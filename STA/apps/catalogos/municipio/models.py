from django.db import models
from apps.catalogos.departamento.models import Departamento

class Municipio(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=3, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    departamento = models.ForeignKey(Departamento, verbose_name= 'Departamento', on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return f'{self.codigo} - {self.descripcion}'