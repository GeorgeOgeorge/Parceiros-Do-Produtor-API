from django.contrib import admin

from .models import Farmer, Propertie, Animal, Milking


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'age',
        'phone',
        'sex',
        'active',
        'created',
        'updated',
        'properties'
    ]


@admin.register(Propertie)
class PropertieAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'phone',
        'longitude',
        'latitude',
        'active',
        'created',
        'updated',
        'animals',
    ]


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'sex',
        'breed',
        'code',
        'furr_color',
        'purchased',
        'birth_date',
        'active',
        'created',
        'updated',
        'milkings',
    ]


@admin.register(Milking)
class MilkingAdmin(admin.ModelAdmin):
    list_display = [
        'value',
        'date',
        'shift',
        'dry',
        'active',
        'created',
        'updated',
    ]
