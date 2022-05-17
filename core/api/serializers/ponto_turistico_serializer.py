from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


class PontoTuristicoSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()
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

        data_endereco = validated_data['endereco']
        del validated_data['endereco']

        ponto_turistico = PontoTuristico.objects.create(**validated_data)

        self.cria_atracoes(atracoes, ponto_turistico)

        novo_endereco = Endereco.objects.create(**data_endereco)
        
        ponto_turistico.endereco = novo_endereco
        ponto_turistico.save()
        return ponto_turistico
