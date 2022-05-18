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

    def aprova_comentarios(self, request, queryset):
        queryset.update(aprovado=True)
    aprova_comentarios.short_description = 'Aprovar comentários selecionados'

    def reprova_comentarios(self, request, queryset):
        queryset.update(aprovado=False)
    reprova_comentarios.short_description = 'Reprovar comentários selecionados'

    actions = [
        'aprova_comentarios',
        'reprova_comentarios',
    ]
