from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(read_only=True)
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
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
    
    def cria_atracoes(self, atracoes, ponto_turistico):
        for atracao in atracoes:
            nova_atracao = Atracao.objects.create(**atracao)
            ponto_turistico.atracoes.add(nova_atracao)

    
    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']
        ponto_turistico = PontoTuristico.objects.create(**validated_data)

        self.cria_atracoes(atracoes, ponto_turistico)

        return ponto_turistico
