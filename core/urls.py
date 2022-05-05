from django.urls import include, path
from rest_framework import routers

from .api.viewsets import PontoTuristicoViewSet

router = routers.DefaultRouter()
router.register('pontoturistico', PontoTuristicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
