from django.urls import path, include
from . import views

urlpatterns = [
    path('exportar_relatorio/', views.relatorios, name='relatorios'),
    path('accounts/', include('allauth.urls')),
    
]