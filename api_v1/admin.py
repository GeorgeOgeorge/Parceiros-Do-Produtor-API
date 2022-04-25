from django.contrib import admin

from .models import Farmer, Animal, Milking, Production, Property

admin.site.register(Farmer)
admin.site.register(Property)
admin.site.register(Production)
admin.site.register(Animal)
admin.site.register(Milking)
