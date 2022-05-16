from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from rest_framework import serializers


class PontoTuristicoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)

    class Meta:
        model = PontoTuristico
        fields = [
            'id',
            'nome',
            'descricao',
            'foto',
            'endereco',
            'aprovado',
            'atracoes',
            'comentarios',
            'avaliacoes',
        ]
