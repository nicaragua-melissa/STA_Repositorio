from django.contrib import admin

from apps.catalogos.rutaCritica.models import RutaCritica

@admin.register(RutaCritica)
class RutaCriticaAdmin(admin.ModelAdmin):
    search_fields = ['id','codigo','descripcion']
    list_display = ['codigo','descripcion']