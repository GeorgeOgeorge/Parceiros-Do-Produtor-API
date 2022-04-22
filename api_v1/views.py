from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework import viewsets

from .models import Animal, Farmer, Milking, Propertie, Herd
from .serializers import AnimalSerializer, FarmerSerializer, MilkingSerializer, PropertieSerializer, HerdSerializer, AutenticacaoSerializer


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer


class PropertieViewSet(viewsets.ModelViewSet):
    queryset = Propertie.objects.all()
    serializer_class = PropertieSerializer


class HerdViewSet(viewsets.ModelViewSet):
    queryset = Herd.objects.all()
    serializer_class = HerdSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class MilkingViewSet(viewsets.ModelViewSet):
    queryset = Milking.objects.all()
    serializer_class = MilkingSerializer

@api_view(['POST'])
def login(request, format=None):

    if request.method == 'POST':
        login = AutenticacaoSerializer(request.data)
        Usuarioresultado = authenticate(username=login.data['usuario'], password=login.data['senha'])
        if Usuarioresultado is not None:
            token = Token.objects.get_or_create(user=Usuarioresultado)
            return Response({"token": token[0].key}, status=status.HTTP_202_ACCEPTED)
        else: return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    else: return Response(status=status.HTTP_400_BAD_REQUEST)
