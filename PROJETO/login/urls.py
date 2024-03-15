from django.urls import path, include
from .views import signin, logado, deslogado

urlpatterns = [
    path('', signin, name='login_funcionario'), #name = nome da path para indicar em outra página que eu vou clicar e ir para essa página
    path('buscarUsuario/', logado, name='logado'),
    path('sair/', deslogado, name='sair'),
    path('', include('alterarConta.urls')),
    #path('alterarConta/', logado, name='logado'),
]