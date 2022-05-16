from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = [
            'id',
            'nome',
            'descricao',
            'descricao_completa',
            'descricao_completa2',
            'foto',
            'endereco',
            'aprovado',
            'atracoes',
            'comentarios',
            'avaliacoes',
        ]

    def get_descricao_completa(self, obj):
        return f'{obj.nome} - {obj.descricao}'
