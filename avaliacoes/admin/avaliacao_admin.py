from django.contrib import admin

from ..models import Avaliacao


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'usuario',
        'comentario',
        'nota',
        'data_criacao'
    ]

    search_fields = [
        'id',
        'usuario__username',
        'usuario__first_name',
        'usuario__last_name',
        'comentario',
        'nota',
        'data_criacao'
    ]

    list_filter = [
        'usuario',
        'data_criacao'
    ]

    autocomplete_fields = [
        'usuario'
    ]
