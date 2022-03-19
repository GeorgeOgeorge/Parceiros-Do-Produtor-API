from rest_framework import viewsets

from .models import Animal, Farmer, Milking, Propertie
from .serializers import AnimalSerializer, FarmerSerializer, MilkingSerializer, PropertieSerializer

# TODO: create path to list relations  

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class PropertieViewSet(viewsets.ModelViewSet):
    queryset = Propertie.objects.all()
    serializer_class = PropertieSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class MilkingViewSet(viewsets.ModelViewSet):
    queryset = Milking.objects.all()
    serializer_class = MilkingSerializer
