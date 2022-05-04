from django.db import models


class Endereco(models.Model):
    '''
    A classe Endereco serve para armazernar os(as) endereços do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Endereco.
    '''

    linha1 = models.CharField(
        verbose_name='Linha 1',
        max_length=100
    )

    linha2 = models.CharField(
        verbose_name='Linha 2',
        max_length=100,
        null=True, blank=True
    )

    cidade = models.CharField(
        verbose_name='Cidade',
        max_length=100
    )

    estado = models.CharField(
        verbose_name='Estado',
        max_length=100
    )

    pais = models.CharField(
        verbose_name='País',
        max_length=100
    )

    latitude = models.BigIntegerField(
        verbose_name='Latitude',
        null=True, blank=True
    )

    longitude = models.BigIntegerField(
        verbose_name='Longitude',
        null=True, blank=True
    )

    def __str__(self):
        return self.linha1

    class Meta:
        app_label = 'enderecos'
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
