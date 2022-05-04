from django.contrib import admin

from ..models import Endereco


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'linha1',
        'linha2',
        'cidade',
        'estado',
        'pais',
        'latitude',
        'longitude'
    ]

    search_fields = [
        'id',
        'linha1',
        'linha2',
        'cidade',
        'estado',
        'pais',
        'latitude',
        'longitude'
    ]

    list_filter = [
        'cidade',
        'estado',
        'pais',
    ]

    # autocomplete_fields = [
        # 'campos_fk
    # ]
