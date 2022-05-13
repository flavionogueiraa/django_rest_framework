from atracoes.models import Atracao
from rest_framework import filters, viewsets

from ..serializers import AtracaoSerializer


class AtracaoViewSet(viewsets.ModelViewSet):
    queryset = Atracao.objects.all()
    
    serializer_class = AtracaoSerializer
    
    filter_backends = [
        filters.SearchFilter,
    ]

    filter_fields = [
        'nome',
        'descricao',
    ]
