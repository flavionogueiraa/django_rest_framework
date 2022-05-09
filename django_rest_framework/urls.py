from atracoes.urls import atracoes_router
from avaliacoes.urls import avaliacoes_router
from comentarios.urls import comentarios_router
from core.urls import core_router
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from enderecos.urls import enderecos_router
from rest_framework import routers

main_router = routers.DefaultRouter()
main_router.registry.extend(atracoes_router.registry)
main_router.registry.extend(core_router.registry)
main_router.registry.extend(enderecos_router.registry)
main_router.registry.extend(comentarios_router.registry)
main_router.registry.extend(avaliacoes_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_router.urls)),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
