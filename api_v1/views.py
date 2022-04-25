from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Animal, Farmer, Milking, Property, Production
from .serializers import AnimalSerializer, FarmerSerializer, MilkingSerializer, PropertySerializer, ProductionSerializer, AutenticacaoSerializer

@csrf_exempt
@api_view(['POST'])
def login(request, format=None):

    if request.method == 'POST':
        login = AutenticacaoSerializer(request.data)
        Usuarioresultado = authenticate(username=login.data['username'], password=login.data['password'])
        if Usuarioresultado is not None:
            token = Token.objects.get_or_create(user=Usuarioresultado)
            return Response({"token": token[0].key}, status=status.HTTP_202_ACCEPTED)
        else: 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
    else: 
        return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'POST'])
def farmer_CR(request, format=None):

    if request.method == 'GET':
        serializer = FarmerSerializer(Farmer.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = FarmerSerializer(data=request.data)
        if serializer.is_valid():
            _saveFarmer(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)

    else: 
        return Response(status=status.HTTP_400_BAD_REQUEST)
       

@api_view(['GET', 'PUT', 'DELETE'])
def farmer_RUD(request, farmer_pk, format=None):
    try: farmer = Farmer.objects.get(pk=farmer_pk)
    except: return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = FarmerSerializer(farmer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = FarmerSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        farmer.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def property_CR(request, format=None):

    if request.method == 'GET':
        serailizer = PropertySerializer(Property.objects.all(), many=True)
        return Response(serailizer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serailizer = PropertySerializer(request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data, status=status.HTTP_201_CREATED)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)
         

@api_view(['GET', 'PUT', 'DELETE'])
def property_RUD(request, property_pk, format=None):
    try: property = Property.objects.get(pk=property_pk)
    except: return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = PropertySerializer(property)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = PropertySerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        property.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def production_CR(request, format=None):

    if request.method == 'GET':
        serailizer = ProductionSerializer(Production.objects.all(), many=True)
        return Response(serailizer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serailizer = ProductionSerializer(request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data, status=status.HTTP_201_CREATED)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)
         

@api_view(['GET', 'PUT', 'DELETE'])
def production_RUD(request, production_pk, format=None):
    try: production = Production.objects.get(pk=production_pk)
    except: return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = ProductionSerializer(production)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = ProductionSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        production.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def animal_CR(request, format=None):

    if request.method == 'GET':
        serailizer = AnimalSerializer(Animal.objects.all(), many=True)
        return Response(serailizer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serailizer = AnimalSerializer(request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data, status=status.HTTP_201_CREATED)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)
         

@api_view(['GET', 'PUT', 'DELETE'])
def animal_RUD(request, animal_pk, format=None):
    try: animal = Animal.objects.get(pk=animal_pk)
    except: return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = AnimalSerializer(animal)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = AnimalSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        animal.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def milking_CR(request, format=None):

    if request.method == 'GET':
        serailizer = MilkingSerializer(Milking.objects.all(), many=True)
        return Response(serailizer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serailizer = Milking(request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data, status=status.HTTP_201_CREATED)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)
         

@api_view(['GET', 'PUT', 'DELETE'])
def milking_RUD(request, milking_pk, format=None):
    try: milking = Milking.objects.get(pk=milking_pk)
    except: return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = MilkingSerializer(milking)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = MilkingSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        milking.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    else: return Response(status=status.HTTP_400_BAD_REQUEST)


def _saveFarmer(serializer):
    farmer = Farmer(
        username=serializer.data['username'], 
        cpf=serializer.data['cpf'], 
        email=serializer.data['email'], 
        age=serializer.data['age'], 
        phone=serializer.data['phone'], 
        sex=serializer.data['sex']
    )
    farmer.set_password(serializer.data['password'])
    farmer.save()