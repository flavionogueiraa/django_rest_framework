from django.contrib import admin

from ..models import Atracao


@admin.register(Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nome',
        'descricao',
        'horario_abertura',
        'horario_fechamento',
        'idade_minima',
    ]

    search_fields = [
        'id',
        'nome',
        'descricao',
        'horario_abertura',
        'horario_fechamento',
        'idade_minima'
    ]

    list_filter = [
        'idade_minima',
    ]

    # autocomplete_fields = [
    #     'campos_fk
    # ]
