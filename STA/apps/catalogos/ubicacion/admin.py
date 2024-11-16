from django.contrib import admin

from apps.catalogos.ubicacion.models import Ubicacion

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['codigo','nombre','direccion']
