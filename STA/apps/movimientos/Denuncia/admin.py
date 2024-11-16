from django.contrib import admin

from apps.movimientos.Denuncia.models import Denuncia, DetalleDenuncia


@admin.register(Denuncia)
class DenunciaAdmin(admin.ModelAdmin):
    search_fields = ['id','codigo']
    list_display = ['codigo','descripcion_persona','descripcion_hechos','direccion','zona','fecha']

@admin.register(DetalleDenuncia)
class DetalleDenunciaAdmin(admin.ModelAdmin):
    search_fields = ['id','codigo']
    list_display = ['codigo','animal',]

