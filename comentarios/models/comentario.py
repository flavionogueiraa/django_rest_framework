from django.contrib.auth.models import User
from django.db import models


class Comentario(models.Model):
    '''
    A classe Comentario serve para armazernar os(as) comentários do sistema.
    Além de fazer as implementações relacionadas a um único objeto do tipo Comentario.
    '''

    comentario = models.TextField(
        verbose_name='Comentário'
    )

    data_criacao = models.DateTimeField(
        verbose_name='Data de criação',
        auto_now_add=True
    )
    
    usuario = models.ForeignKey(
        User,
        verbose_name='Usuário',
        on_delete=models.CASCADE
    )

    aprovado = models.BooleanField(
        verbose_name='Aprovado',
        default=True
    )

    def __str__(self):
        return self.comentario

    class Meta:
        app_label = 'comentarios'
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
