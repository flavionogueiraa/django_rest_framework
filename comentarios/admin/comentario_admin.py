from django.contrib import admin

from ..models import Comentario


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'comentario',
        'data_criacao',
        'usuario',
        'aprovado'
    ]

    search_fields = [
        'id',
        'comentario',
        'data_criacao',
        'usuario__username',
        'usuario__first_name',
        'usuario__last_name',
        'aprovado'
    ]

    list_filter = [
        'data_criacao',
        'usuario',
        'aprovado'
    ]

    autocomplete_fields = [
        'usuario'
    ]
