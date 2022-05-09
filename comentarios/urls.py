from django.urls import path
from rest_framework import routers

from .api.viewsets import ComentarioViewSet

comentarios_router = routers.DefaultRouter()
comentarios_router.register('comentarios', ComentarioViewSet)

urlpatterns = [
    
]
