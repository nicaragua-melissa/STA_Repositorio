from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.catalogos.camara.models import Camara
from apps.catalogos.camara.API.serializers import CamaraSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

class CamaraApiView(APIView):
    """
    Vista para listar todas las camaras, agregar una nueva, actualizar o eliminar una por ID.
    """
    @swagger_auto_schema(responses={200: CamaraSerializer(many=True)})
    def get(self, request):
        """
        Listar todas las camaras.
        """
        camaras = Camara.objects.all()
        serializer = CamaraSerializer(camaras, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=CamaraSerializer, responses={201: CamaraSerializer})
    def post(self, request):
        """
        Agregar una nueva camara
        """
        serializer = CamaraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=CamaraSerializer, responses={200: CamaraSerializer})
    def patch(self, request, pk):
        """
        Actualizar parcialmente una camara existente por su ID
        """
        try:
            camara = Camara.objects.get(pk=pk)
        except Camara.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CamaraSerializer(camara, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'No Content'})
    def delete(self, request, pk):
        """
        Eliminar una camara por su ID.
        """
        try:
            camara = Camara.objects.get(pk=pk)
        except Camara.DoesNotExist:
            return Response({'error': 'Camara no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        camara.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)