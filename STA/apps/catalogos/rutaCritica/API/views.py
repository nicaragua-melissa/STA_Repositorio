from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.rutaCritica.models import RutaCritica
from apps.catalogos.rutaCritica.API.serializers import RutaCriticaSerializer
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.seguridad.permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers


# Configura el logger
logger = logging.getLogger(__name__)




class RutaCriticaApiView(PaginationMixin, APIView):
    """
    Vista para listar todas las rutas o agregar una nueva.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = RutaCritica


    @swagger_auto_schema(responses={200: RutaCriticaSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las rutas.
        """
        logger.info("GET request to list all rutas")
        rutas = RutaCritica.objects.all().order_by('id')
        page = self.paginate_queryset(rutas, request)

        if page is not None:
            serializer = RutaCriticaSerializer(page, many=True)
            logger.info("Paginated response for rutas criticas")
            return self.get_paginated_response(serializer.data)

        serializer = RutaCriticaSerializer(rutas, many=True)
        logger.error("Returning all rutas without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RutaCriticaSerializer, responses={201: RutaCriticaSerializer})
    def post(self, request):
        """
        Agregar una nueva ruta
        """
        logger.info("POST request to create a new ruta")

        serializer = RutaCriticaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Ruta created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create ruta: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RutaCriticaDetails(APIView):
    """
        Vista para obtener, actualizar o eliminar una ruta específica.
        """

    permission_classes = [IsAuthenticated, CustomPermission]
    model = RutaCritica

    @swagger_auto_schema(request_body=RutaCriticaSerializer, responses={200: RutaCriticaSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar completamente una ruta por su ID.
        """
        logger.info("PUT request to update ruta with ID: %s", pk)
        ruta = get_object_or_404(RutaCritica, id=pk)
        if not ruta:
            return Response({'error': 'Ruta Critica no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, ruta)  # Verificación de permisos
        serializer = RutaCriticaSerializer(ruta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Ruta Critica updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to update ruta with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(request_body=RutaCriticaSerializer, responses={200: RutaCriticaSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una ruta existente por su ID
        """

        logger.info("PATCH request to partially update ruta with ID: %s", pk)
        ruta = get_object_or_404(RutaCritica, id=pk)

        if not ruta:
            return Response({'error': 'Ruta Critica no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, ruta)  # Verificación de permisos
        serializer = RutaCriticaSerializer(ruta, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Ruta Critica partially updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to partially update ruta with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una ruta por su ID.
        """
        logger.info("DELETE request to delete ruta with ID: %s", pk)
        ruta = get_object_or_404(RutaCritica, id=pk)
        if not ruta:
            return Response({'error': 'Ruta no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, ruta)  # Verificación de permisos
        ruta.delete()
        logger.info("Ruta Critica deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)