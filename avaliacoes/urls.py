from django.urls import path
from rest_framework import routers

from .api.viewsets import AvaliacaoViewSet

avaliacoes_router = routers.DefaultRouter()
avaliacoes_router.register('avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    
]
