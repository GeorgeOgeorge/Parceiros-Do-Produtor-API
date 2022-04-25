from rest_framework import serializers

from .models import Farmer, Animal, Milking, Property, Production


class AutenticacaoSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


class FarmerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farmer
        fields = [
            'id', 'username', 'cpf', 
            'email', 'age', 'phone', 
            'sex', 'active', 'password'
        ]
        extra_kargs = {
            'id': {'read_only': True},
            'cpf': {'write_only': True},
            'properties': {'read_only': True},
            'active': {'read_only': True}
        }


class PropertySerializer(serializers.ModelSerializer):

    productions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True, 
        view_name='production-detail'
    )

    class Meta:
        model = Property
        fields = [
            'id', 'farmer', 'name',
            'phone', 'longitude', 'latitude',
            'size', 'active', 'productions'
        ]
        extra_kargs = {'productions': {'read_only': True}}


class ProductionSerializer(serializers.ModelSerializer):

    animals = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='animal-detail'
    )

    class Meta:
        model = Production
        fields = [
            'id', 'property', 'name',
            'animal_type', 'warning', 'log',
            'identified_animals', 'active', 'animals'
        ]
        extra_kargs = {'animals': {'read_only': True}}


class AnimalSerializer(serializers.ModelSerializer):

    milkings = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='milking-detail'
    )

    class Meta:
        model = Animal
        fields = [
            'id', 'name', 'production',
            'sex', 'breed', 'code', 
            'furr_color','purchased', 'birth_date',
            'active', 'milkings'
        ]
        extra_kargs = {'milkings': {'read_only': True}}


class MilkingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milking
        fields = [
            'id', 'value', 'animal',
            'date', 'shift', 'dry',
            'active'
        ]
