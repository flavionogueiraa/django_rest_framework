from django.contrib.auth.models import User
from django.db import models


class Avaliacao(models.Model):
    '''
    A classe Avaliacao serve para armazernar os(as) avaliações do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Avaliacao.
    '''

    usuario = models.ForeignKey(
        User,
        verbose_name='Usuário',
        on_delete=models.CASCADE
    )

    comentario = models.TextField(
        verbose_name='Comentário',
        null=True, blank=True
    )

    nota = models.DecimalField(
        verbose_name='Nota',
        max_digits=3, decimal_places=1
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )

    def __str__(self):
        return self.usuario.username

    class Meta:
        app_label = 'avaliacoes'
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
