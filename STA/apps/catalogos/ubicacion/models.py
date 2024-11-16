from django.db import models

class Ubicacion(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=5, unique=True)
    nombre = models.CharField(verbose_name='Nombre', max_length=60)
    direccion = models.CharField(verbose_name='Dirección', max_length=1000)

    class Meta:
        verbose_name_plural = 'Ubicaciones'

    def __str__(self):
        return f'{self.codigo} - {self.nombre}'