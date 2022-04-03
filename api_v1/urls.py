from django.db import router

from rest_framework.routers import SimpleRouter

from .views import FarmerViewSet, AnimalViewSet, MilkingViewSet, PropertieViewSet, HerdViewSet

router = SimpleRouter()
router.register('farmers', FarmerViewSet)
router.register('properties', PropertieViewSet)
router.register('animals', AnimalViewSet)
router.register('milkings', MilkingViewSet)
router.register('herds', HerdViewSet)