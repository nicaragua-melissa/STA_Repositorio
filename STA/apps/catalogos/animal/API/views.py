from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.animal.models import Animal
from apps.catalogos.animal.API.serializers import AnimalSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

class AnimalApiView(APIView):
    """
    Vista para listar todos los animales, agregar uno nuevo, actualizar o eliminar.
    """
    @swagger_auto_schema(responses={200: AnimalSerializer(many=True)})
    def get(self, request):
        """
        Listar todos los animales.
        """
        animales = Animal.objects.all()
        serializer = AnimalSerializer(animales, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=AnimalSerializer, responses={201: AnimalSerializer})
    def post(self, request):
        """
        Agregar un nuevo animal
        """
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=AnimalSerializer, responses={200: AnimalSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente un animal existente por su ID
        """
        try:
            animal = Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AnimalSerializer(animal, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar un animal por su ID.
        """
        try:
            animal = Animal.objects.get(pk=pk)
        except Animal.DoesNotExist:
            return Response({'error': 'Animal no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
