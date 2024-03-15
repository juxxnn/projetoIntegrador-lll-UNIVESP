from django.urls import path
from .views import criarConta, sucesso

urlpatterns = [
    path('criarConta/', criarConta, name='cadastro_funcionario'),
    path('sucesso/', sucesso, name='sucesso'),
]