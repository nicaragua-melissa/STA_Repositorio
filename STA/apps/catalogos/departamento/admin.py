from django.contrib import admin

from apps.catalogos.departamento.models import Departamento

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    search_fields = ['id','descripcion']
    list_display = ['codigo','descripcion']
