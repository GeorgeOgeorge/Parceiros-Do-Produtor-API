from rest_framework import viewsets

from .models import Animal, Farmer, Milking, Propertie, Herd
from .serializers import AnimalSerializer, FarmerSerializer, MilkingSerializer, PropertieSerializer, HerdSerializer


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
