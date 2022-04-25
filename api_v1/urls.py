from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path

from .views import (
    login, farmer_CR, farmer_RUD, property_CR, property_RUD, 
    production_CR, production_RUD, animal_CR, animal_RUD, milking_CR, milking_RUD
)
 
urlpatterns = [
    path('login/', login),
    path('farmers/', farmer_CR),
    path('farmers/<int:farmer_pk>/', farmer_RUD),
    path('properties/', property_CR),
    path('properties/<int:property_pk>', property_RUD),
    path('production/', production_CR),
    path('production/<int:production_pk>', production_RUD),
    path('animals/', animal_CR),
    path('animals/<int:animal_pk>', animal_RUD),
    path('milkings/', milking_CR),
    path('milkings/<int:milking_pk>', milking_RUD)
]

urlpatterns = format_suffix_patterns(urlpatterns)
