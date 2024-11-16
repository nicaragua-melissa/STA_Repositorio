from django.contrib import admin

from apps.catalogos.animal.models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    search_fields = ['id','nombre']
    list_display = ['codigo','nombre']