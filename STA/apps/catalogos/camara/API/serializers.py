from rest_framework import serializers
from apps.catalogos.camara.models import Camara


class CamaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camara
        fields = '__all__'