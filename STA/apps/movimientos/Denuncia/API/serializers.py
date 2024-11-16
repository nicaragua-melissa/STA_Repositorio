from rest_framework.serializers import ModelSerializer, CharField
from apps.movimientos.Denuncia.models import Denuncia,DetalleDenuncia
from apps.catalogos.animal.API.serializers import AnimalSerializer
from apps.catalogos.rutaCritica.API.serializers import RutaCriticaSerializer

# Serializador de la clase DetalleDenuncia
class DetalleDenunciaSerializer(ModelSerializer):
    animal_nombre = CharField(source='animal.nombre', read_only=True)
    class Meta:
        model = DetalleDenuncia
        fields = ['codigo','animal','animal_nombre']

# Serializador de la clase Denuncia
class DenunciaSerializer(ModelSerializer):
    ruta_nombre = RutaCriticaSerializer(read_only=True)
    # ruta_nombre = CharField(source='ruta.descripcion', read_only=True)
    tipo_nombre = CharField(source='tipo.descripcion', read_only=True)
    detalles = DetalleDenunciaSerializer(many=True)
    class Meta:
        model = Denuncia
        fields = ['codigo', 'descripcion_persona', 'descripcion_hechos', 'direccion', 'zona', 'rutaCritica',
                  'ruta_nombre','tipoDenuncia', 'tipo_nombre' ,'detalles']