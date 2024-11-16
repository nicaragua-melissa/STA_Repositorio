from rest_framework import serializers
from apps.catalogos.rutaCritica.models import RutaCritica


class RutaCriticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutaCritica
        fields = '__all__'