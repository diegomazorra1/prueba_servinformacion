from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsuarioSerializer, CreateUsuarioSerializer
from .models import Usuarios
# Create your views here.


@api_view(['GET'])
def usuarios_lista(request):
    circle= Usuarios.objects.all()
    serializer= UsuarioSerializer(circle,many=True)

    return Response(serializer.data)



@api_view(['POST'])
def usuarios_create(request):
    serializer= CreateUsuarioSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data=serializer.save()
    create= Usuarios.objects.create(**data)


    return Response(UsuarioSerializer(create).data)
