from django.contrib import admin

from apps.catalogos.tipoDenuncia.models import TipoDenuncia

@admin.register(TipoDenuncia)
class TipoDenunciaAdmin(admin.ModelAdmin):
    search_fields = ['id','descripcion']
    list_display = ['codigo','descripcion']
