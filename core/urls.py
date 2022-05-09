from django.urls import include, path
from rest_framework import routers

from .api.viewsets import PontoTuristicoViewSet

core_router = routers.DefaultRouter()
core_router.register('pontos-turisticos', PontoTuristicoViewSet)

urlpatterns = [
    
]
