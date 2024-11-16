from rest_framework import serializers
from apps.catalogos.animal.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'