from django.urls import path
from alterarConta.views import alterarConta, salvaAltera

urlpatterns = [
    path('alterarConta/', alterarConta, name='alterar_conta'),
    path('alterarConta/<str:func_id>/', alterarConta, name='alterar_cadastro'),
    path('alterarConta/<str:func_id>/salvar_alteracoes/', salvaAltera, name='salvar_alteracoes'),
]