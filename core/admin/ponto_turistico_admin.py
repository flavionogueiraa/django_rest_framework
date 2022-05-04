from django.contrib import admin

from ..models import PontoTuristico


@admin.register(PontoTuristico)
class PontoTuristicoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'descricao',
        'aprovado'
    ]

    search_fields = [
        'id',
        'nome',
        'descricao',
        'aprovado'
    ]

    list_filter = [
        'aprovado'
    ]

    filter_horizontal = [
        'atracoes',
        'comentarios',
        'avaliacoes'
    ]

    # autocomplete_fields = [
    #     'campos_fk
    # ]
