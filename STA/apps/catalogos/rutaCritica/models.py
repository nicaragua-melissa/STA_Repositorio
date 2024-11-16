from django.db import models
from apps.catalogos.nivelRuta.models import NivelRuta
from apps.catalogos.municipio.models import Municipio

class RutaCritica(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=5, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=100)
    municipio = models.ForeignKey(Municipio, verbose_name= 'Municipio', on_delete=models.PROTECT)
    nivelRuta = models.ForeignKey(NivelRuta, verbose_name= 'Nivel de Ruta', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Rutas Críticas'

    def __str__(self):
        return f'{self.codigo} - {self.descripcion}'
