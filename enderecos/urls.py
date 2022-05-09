from django.urls import path
from rest_framework import routers

from .api.viewsets import EnderecoViewSet

enderecos_router = routers.DefaultRouter()
enderecos_router.register('enderecos', EnderecoViewSet)

urlpatterns = [
    
]
