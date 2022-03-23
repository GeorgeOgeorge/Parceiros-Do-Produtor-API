from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Animal, Farmer, Milking, Propertie
from .serializers import AnimalSerializer, FarmerSerializer, MilkingSerializer, PropertieSerializer

# TODO: create path to list relations  

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

    @action(detail=True, methods=['get'])
    def properties(self, request, pk=None):
        properties = Propertie.objects.filter(id=pk)
        serializer = PropertieSerializer(properties.all(), many=True)
        return Response(serializer.data)


class PropertieViewSet(viewsets.ModelViewSet):
    queryset = Propertie.objects.all()
    serializer_class = PropertieSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

class MilkingViewSet(viewsets.ModelViewSet):
    queryset = Milking.objects.all()
    serializer_class = MilkingSerializer
