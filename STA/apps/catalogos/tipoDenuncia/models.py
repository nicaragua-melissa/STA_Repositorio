from django.db import models

class TipoDenuncia(models.Model):
    codigo = models.CharField(verbose_name='Código', max_length=5, unique=True)
    descripcion = models.CharField(verbose_name='Descripción', max_length=50)
    class Meta:
        verbose_name_plural = 'Tipos de Denuncia'

    def __str__(self):
        return f'{self.codigo} - {self.descripcion}'