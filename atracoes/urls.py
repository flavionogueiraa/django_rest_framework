from django.urls import path
from rest_framework import routers

from .api.viewsets import AtracaoViewSet

atracoes_router = routers.DefaultRouter()
atracoes_router.register('atracao', AtracaoViewSet)

urlpatterns = [
    
]
