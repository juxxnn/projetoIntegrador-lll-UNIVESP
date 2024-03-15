from django.urls import path
from . import views

urlpatterns = [
    # ... outras URLs ...
    path('logado/', views.logado, name='logado'),
]