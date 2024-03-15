from django.urls import path
from criarUsuario.views import editarUsuario, passo1, passo2, passo3, passo4
from . import views

urlpatterns = [
    path('editarUsuario/<int:usuario_id>/', editarUsuario, name='editar_usuario'), 
    path('buscar_endereco/', views.buscar_endereco, name='buscar_endereco'),

    path('passo1/', passo1 , name='criar_usuario'),
    path('passo1/', passo1 , name='passo_um'),
    path('passo2/', passo2 , name='passo_dois'),
    path('passo3/', passo3 , name='passo_tres'),
    path('passo4/', passo4 , name='passo_quatro'),
]