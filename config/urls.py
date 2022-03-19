from django.contrib import admin
from django.urls import path, include
from rest_framework import urls

from api_v1.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(urls)),
    path('amigos_produtor/', include(router.urls)),
]
