from apps.catalogos.rutaCritica.models import RutaCritica
from apps.catalogos.ubicacion.models import Ubicacion
from django.db import models

class Camara(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=5, unique=True)
    recording_Start = models.DateTimeField(verbose_name='Recording Start')
    recording_End = models.DateTimeField(verbose_name='Recording End')
    estado = models.CharField(verbose_name='Estado',max_length=16)
    ubicacion = models.ForeignKey(Ubicacion, verbose_name= 'Ubicación', on_delete=models.PROTECT)
    rutaCritica = models.ForeignKey(RutaCritica, verbose_name= 'Ruta Crítica', on_delete=models.PROTECT)
    class Meta:
        verbose_name_plural = 'Cámaras'

    def __str__(self):
        return f'{self.codigo} - {self.estado}'