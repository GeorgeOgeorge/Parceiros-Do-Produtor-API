from django.db import router
from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import FarmerViewSet, AnimalViewSet, MilkingViewSet, PropertieViewSet

router = SimpleRouter()
router.register('farmers', FarmerViewSet)
router.register('properties', PropertieViewSet)
router.register('animals', AnimalViewSet)
router.register('milkings', MilkingViewSet)