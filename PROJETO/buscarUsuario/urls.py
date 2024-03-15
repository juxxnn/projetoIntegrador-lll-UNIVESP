from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from buscarUsuario.views import buscarUsuario, credencial, exclui_usuario

urlpatterns = [
    path('pesquisa', buscarUsuario, name='pesquisa'),
    path('buscarUsuario/', buscarUsuario, name='buscar_usuario'),

    path('credencial', credencial, name='credencial'),
    path('credencial/<int:usuario_id>/', credencial, name='gera_credencial'),
    path('exclui_usuario/<int:usuario_id>/', exclui_usuario, name='exclui_usuario'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)