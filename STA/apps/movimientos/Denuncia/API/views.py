from django.db import models, transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.movimientos.Denuncia.models import Denuncia, DetalleDenuncia
from apps.movimientos.Denuncia.API.serializers import DenunciaSerializer, DetalleDenunciaSerializer
from apps.catalogos.rutaCritica.models import RutaCritica
from apps.catalogos.tipoDenuncia.models import TipoDenuncia
from apps.catalogos.animal.models import Animal
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.seguridad.permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers


# Configura el logger
logger = logging.getLogger(__name__)



# Vista para manejar Denuncias
class DenunciaApiView(PaginationMixin, APIView):
    """
       Vista para listar todas las denuncias y crear una nueva.
       """

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Denuncia


    @swagger_auto_schema(responses={200: DenunciaSerializer(many=True)})
    def get(self, request):
        """
        Obtener una lista de todas las denuncias.
        """
        logger.info("GET request to list all denuncias")
        denuncias = Denuncia.objects.all().order_by('id')
        page = self.paginate_queryset(denuncias, request)

        if not denuncias:
            return Response({"detail": "No se encontraron denuncias."}, status=status.HTTP_404_NOT_FOUND)

        if page is not None:
            serializer = DenunciaSerializer(page, many=True)
            logger.info("Paginated response for denuncias")
            return self.get_paginated_response(serializer.data)

        serializer = DenunciaSerializer(denuncias, many=True)
        logger.error("Returning all denuncias without pagination")
        return Response(serializer.data, status=status.HTTP_200_OK)



    """
    Vista para listar todas las denuncias o crear una nueva.  
    """
    @swagger_auto_schema(request_body=DenunciaSerializer)
    def post(self, request):
        serializer = DenunciaSerializer(data=request.data)

        if serializer.is_valid():
            try:
                with transaction.atomic():
                    # Validar si el código de denuncia ya existe
                    codigo = serializer.validated_data['codigo']
                    if Denuncia.objects.filter(codigo=codigo).exists():
                        return Response({'Error': 'La denuncia ya existe.'}, status=status.HTTP_400_BAD_REQUEST)

                    rutaCritica = get_object_or_404(RutaCritica, pk=serializer.validated_data['rutaCritica'].id)
                    tipoDenuncia = get_object_or_404(TipoDenuncia, pk=serializer.validated_data['tipoDenuncia'].id)
                    detalles_data = serializer.validated_data.get('detalles', [])

                    # Creación de la instancia de Denuncia
                    denuncia = Denuncia.objects.create(
                        codigo=serializer.validated_data['codigo'],
                        descripcion_persona=serializer.validated_data['descripcion_persona'],
                        descripcion_hechos=serializer.validated_data['descripcion_hechos'],
                        direccion=serializer.validated_data['direccion'],
                        zona=serializer.validated_data['zona'],
                        rutaCritica=rutaCritica,
                        tipoDenuncia=tipoDenuncia
                    )

                    # Creación de cada DetalleDenuncia
                    for detalle_data in detalles_data:
                        animal = get_object_or_404(Animal, pk=detalle_data['animal'].id)
                        DetalleDenuncia.objects.create(
                            codigo=detalle_data['codigo'],
                            animal=animal,
                            denuncia=denuncia
                        )

                    # Serializar la respuesta
                    denuncia_serializer = DenunciaSerializer(denuncia)
                    return Response(denuncia_serializer.data, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({'Error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DenunciaDetailApiView(APIView):
    """
     Vista para obtener el detalle de una denuncia específica.
     """

    @swagger_auto_schema(responses={200: DenunciaSerializer()})
    def get(self, request, pk):
        """
        Obtener el detalle de una denuncia específica.
        """
        try:
            denuncia = Denuncia.objects.get(pk=pk)
        except Denuncia.DoesNotExist:
            return Response({"detail": "La denuncia con el ID especificado no fue encontrada."},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = DenunciaSerializer(denuncia)
        return Response(serializer.data, status=status.HTTP_200_OK)