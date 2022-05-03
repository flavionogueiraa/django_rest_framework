from atracoes.models import Atracao
from django.db import models


class PontoTuristico(models.Model):
    '''
    A classe PontoTuristico serve para armazernar os(as) pontos turísticos do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo PontoTuristico.
    '''

    nome = models.CharField(
        verbose_name='Nome',
        max_length=100
    )

    descricao = models.TextField(
        verbose_name='Descrição'
    )

    aprovado = models.BooleanField(
        verbose_name='Aprovado',
        default=False
    )

    atracoes = models.ManyToManyField(
        Atracao,
        verbose_name='Atrações'
    )

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Ponto turístico'
        verbose_name_plural = 'Pontos turísticos'