from comentarios.models import Comentario
from rest_framework import viewsets

from ..serializers import ComentarioSerializer


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
