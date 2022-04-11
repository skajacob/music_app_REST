from shutil import register_unpack_format
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
# Create your views 

class HelloApiView(APIView):
    """API View de Prueba""" 
    serializers_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Retornar lista de caractristicas del APIView"""
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django',
            'Nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manualmente a los URLs',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self, request):
        """Crea un mensaje con nuestro nombre"""
        serializer = self.serializers_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Manejo actualizar un objeto"""
        return Response({'method':'PUT'})
    
    def patch(self, request, pk=None):
        """Maneja actualizacion parcial de un objeto"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Borrar un Objeto"""
        return Response({'method':'DELETE'})