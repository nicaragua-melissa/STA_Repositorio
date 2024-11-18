from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.animal.models import Animal
from apps.catalogos.animal.API.serializers import AnimalSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from apps.seguridad.permissions import CustomPermission
from config.utils.Pagination import PaginationMixin
import logging.handlers


# Configura el logger
logger = logging.getLogger(__name__)


class AnimalApiView(PaginationMixin, APIView):
    """
    Vista para listar todos los animales, agregar uno nuevo, actualizar o eliminar.
    """
    permission_classes = [IsAuthenticated, CustomPermission]
    model = RutaCritica


    @swagger_auto_schema(responses={200: AnimalSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los animales.
        """
        logger.info("GET request to list all animales")
        animales = Animal.objects.all().order_by('id')
        page = self.paginate_queryset(animales, request)

        if page is not None:
            serializer = AnimalSerializer(page, many=True)
            logger.info("Paginated response for animales")
            return self.get_paginated_response(serializer.data)

        serializer = AnimalSerializer(animales, many=True)
        logger.error("Returning all animales without pagination")
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AnimalSerializer, responses={201: AnimalSerializer})
    def post(self, request):
        """
        Agregar un nuevo animal
        """
        logger.info("POST request to create a new animal")

        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Animal created successfully")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Failed to create animal: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnimalDetails(APIView):
    """
         Vista para obtener, actualizar o eliminar un animal específico.
    """

    permission_classes = [IsAuthenticated, CustomPermission]
    model = Animal

    @swagger_auto_schema(request_body=AnimalSerializer, responses={200: AnimalSerializer(many=True)})
    def put(self, request, pk):
        """
        Actualizar completamente un animal por su ID.
        """
        logger.info("PUT request to update animal with ID: %s", pk)
        animal = get_object_or_404(RutaCritica, id=pk)
        if not animal:
            return Response({'error': 'Animal no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, animal)  # Verificación de permisos
        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Animal updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to update animal with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=AnimalSerializer, responses={200: AnimalSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un animal existente por su ID
        """

        logger.info("PATCH request to partially update animal with ID: %s", pk)
        animal = get_object_or_404(Animal, id=pk)

        if not animal:
            return Response({'error': 'Animal no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, animal)  # Verificación de permisos
        serializer = AnimalSerializer(animal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info("Animal partially updated successfully with ID: %s", pk)
            return Response(serializer.data)

        logger.error("Failed to partially update animal with ID: %s. Errors: %s", pk, serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un animal por su ID.
        """
        logger.info("DELETE request to delete animal with ID: %s", pk)
        animal = get_object_or_404(Animal, id=pk)
        if not animal:
            return Response({'error': 'Animal no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        self.check_object_permissions(request, animal)  # Verificación de permisos
        animal.delete()
        logger.info("Animal deleted successfully with ID: %s", pk)
        return Response(status=status.HTTP_204_NO_CONTENT)