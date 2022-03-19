from rest_framework import serializers
import datetime

from .models import Farmer, Animal, Milking, Propertie


class FarmerSerializer(serializers.ModelSerializer):

    properties = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='propertie-detail'
    )

    class Meta:
        model = Farmer
        fields = [
            'id',
            'name',
            'age',
            'phone',
            'sex',
            'active',
            'created',
            'updated',
            'properties'
        ]
        extra_kargs = {
            'cpf': {'write_only': True},
            'created': {'read_only': True},
            'updated': {'read_only': True},
            'properties': {'read_only': True}
        }

    def validate_age(self, value):
        if value in range(18, 100):
            return value
        else:
            raise serializers.ValidationError('age must be between 18 to 100')

    def validate_phone(self, value):
        if len(value) == 11:
            return value
        else:
            raise serializers.ValidationError('phone must be 11 characters')

    def validate_name(self, value):
        if len(value) in range(3, 255):
            return value
        else:
            raise serializers.ValidationError('name must be between 3 to 255')

    def validate_cpf(self, value):
        if len(value) == 11:
            return value
        else:
            raise serializers.ValidationError('CPF must have 11 characters')

    def validade_sex(self, value):
        if value is not None:
            return value
        else:
            raise serializers.ValidationError('must specify sex')


class PropertieSerializer(serializers.ModelSerializer):

    animals = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='animal-detail'
    )

    class Meta:
        model = Propertie
        fields = [
            'id',
            'name',
            'phone',
            'longitude',
            'latitude',
            'active',
            'created',
            'updated',
            'animals'
        ]
        extra_kargs = {
            'created': {'read_only': True},
            'updated': {'read_only': True},
            'properties': {'read_only': True}
        }

    def validate_name(self, value):
        if len(value) in range(5, 255):
            return value
        else:
            raise serializers.ValidationError('name must be between 5 to 255')

    def validate_phone(self, value):
        if len(value) == 10:
            return value
        else:
            raise serializers.ValidationError('phone must be 10 characters')


class AnimalSerializer(serializers.ModelSerializer):

    milkings = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='milking-detail'
    )

    class Meta:
        model = Animal
        fields = [
            'id',
            'name',
            'sex',
            'breed',
            'code',
            'furr_color'
            'purchased',
            'birth_date',
            'active',
            'created',
            'updated',
            'milkings'
        ]
        extra_kargs = {
            'created': {'read_only': True},
            'updated': {'read_only': True},
            'properties': {'read_only': True}
        }

    def validate_name(self, value):
        if len(value) in range(3, 255):
            return value
        else:
            raise serializers.ValidationError('name must be between 3 to 255')

    def validate_sex(self, value):
        if value is not None:
            return value
        else:
            raise serializers.ValidationError('must specify sex')

    def validate_breed(self, value):
        if len(value) in range(3, 255):
            return value
        else:
            raise serializers.ValidationError(
                'breed name must be between 3 to 255')

    def validate_code(self, value):
        if value is not None:
            return value
        else:
            raise serializers.ValidationError('must specify animal code')

    def validate_furr_color(self, value):
        if len(value) in range(3, 255):
            return value
        else:
            raise serializers.ValidationError(
                'furr color name must be between 3 to 255')

    def validate_purchased(self, value):
        if value is not None:
            return value
        else:
            raise serializers.ValidationError(
                'must specify is animal is purchased')

    def validate_birth_date(self, value):
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
            return value
        except:
            raise serializers.ValidationError(
                'correct date format is yyyy-mm-dd')


class MilkingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milking
        fields = [
            'id',
            'value',
            'date',
            'shift',
            'dry'
            'active',
            'created',
            'updated',
        ]
        extra_kargs = {
            'created': {'read_only': True},
            'updated': {'read_only': True},
            'properties': {'read_only': True}
        }

    def validate_value(self, value):
        if value is not None:
            return value
        else:
            raise serializers.ValidationError(
                'must specify amount collected during milking, if none specify as 0')

    def validate_date(self, value):
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
            return value
        except:
            raise serializers.ValidationError(
                'correct date format is yyyy-mm-dd')

    def validate_shift(self, value):
        if value is not None:
            return value
        else:
            raise serializers.ValidationError('must specify a shift')

    def validate_dry(self, value):
        if value is not None:
            return value
        else:
            raise serializers.ValidationError('must speficy if animal is dry')
