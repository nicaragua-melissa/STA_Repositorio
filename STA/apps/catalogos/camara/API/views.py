from config.utils.Pagination import PaginationMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.camara.models import Camara
from apps.catalogos.camara.API.serializers import CamaraSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from apps.seguridad.permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers


# Configura el logger
logger = logging.getLogger(__name__)


class CamaraApiView(PaginationMixin, APIView):
    """
    Vista para listar todas las camaras, agregar una nueva, actualizar o eliminar una por ID.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Animal

    @swagger_auto_schema(responses={200: CamaraSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las camaras.
        """
        logger.info("GET request to list all camaras")
        camaras = Camara.objects.all().order_by('id')
        page = self.paginate_queryset(camaras, request)

        if page is not None:
            serializer = CamaraSerializer(page, many=True)
            logger.info("Paginated response for camaras")
            return self.get_paginated_response(serializer.data)

        serializer = CamaraSerializer(camaras, many=True)
        logger.error("Returning all camaras without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CamaraSerializer, responses={201: CamaraSerializer})
    def post(self, request):
        """
        Agregar una nueva camara
        """
        logger.info("POST request to create a new camara")

        serializer = CamaraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Camara created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create camara: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CamaraDetails(APIView):
    """
          Vista para obtener, actualizar o eliminar una camara específica.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = Camara

    @swagger_auto_schema(request_body=CamaraSerializer, responses={200: CamaraSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar completamente una camara por su ID.
        """
        logger.info("PUT request to update camara with ID: %s", pk)
        camara = get_object_or_404(RutaCritica, id=pk)
        if not camara:
            return Response({'error': 'Camara no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, camara)  # Verificación de permisos
        serializer = CamaraSerializer(camara, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Camara updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to update camara with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CamaraSerializer, responses={200: CamaraSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una camara existente por su ID
        """
        logger.info("PATCH request to partially update camara with ID: %s", pk)
        camara = get_object_or_404(Camara, id=pk)

        if not camara:
            return Response({'error': 'Camara no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, camara)  # Verificación de permisos
        serializer = CamaraSerializer(camara, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Camara partially updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to partially update camara with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una camara por su ID.
        """
        logger.info("DELETE request to delete camara with ID: %s", pk)
        camara = get_object_or_404(Camara, id=pk)
        if not camara:
            return Response({'error': 'Camara no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, camara)  # Verificación de permisos
        camara.delete()
        logger.info("Camara deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)