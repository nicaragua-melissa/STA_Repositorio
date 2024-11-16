from django.contrib import admin

from apps.catalogos.especie.models import Especie

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    search_fields = ['id','descripcion']
    list_display = ['codigo','descripcion']
