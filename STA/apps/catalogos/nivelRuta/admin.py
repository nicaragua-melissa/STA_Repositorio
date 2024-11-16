from django.contrib import admin

from apps.catalogos.nivelRuta.models import NivelRuta

@admin.register(NivelRuta)
class NivelRutaAdmin(admin.ModelAdmin):
    search_fields = ['id','descripcion']
    list_display = ['codigo','descripcion']
