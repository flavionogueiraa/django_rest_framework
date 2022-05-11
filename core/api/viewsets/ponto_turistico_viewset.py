from core.models import PontoTuristico
from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    # def list(self, request, *args, **kwargs):
    #     return Response({
    #         'teste': 'É só um teste'
    #     })

    def create(self, request, *args, **kwargs):
        return Response({
            'Hello': request.data['nome']
        })
