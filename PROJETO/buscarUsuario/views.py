from django.shortcuts import render, get_object_or_404

from setup import settings
from .forms import SearchForm
from django.contrib import messages
from django.db.models import Q
from criarUsuario.models import Usuario
from django.contrib.auth import authenticate, login
import os

def buscarUsuario(request):
    form = SearchForm(request.GET or None)
    results = []

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            consulta = form.cleaned_data['consulta']            

            # Busca feita nos campos 'eol' e 'nome_completo'
            try:
                eol_consulta = int(consulta)
                results = Usuario.objects.filter(Q(nome_completo__icontains=consulta) | Q(eol=eol_consulta))
            except ValueError:
                results = Usuario.objects.filter(Q(nome_completo__icontains=consulta) | Q(nome_completo__icontains=str(consulta)))

            results = results.order_by('nome_completo')

    return render(request, 'buscarUsuario/buscar_usuario.html', {'form': form, 'results': results})

def credencial(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    #caminho = usuario.foto3x4.path #obter o 'path' da imagem
    #filename = os.path.basename(caminho) #extrair o nome da imagem

    context = {
        'usuario': usuario,
        #'MEDIA_URL': settings.MEDIA_URL,
        #'filename': filename
    }
    return render (request, 'credencial/credencial.html', context)

def exclui_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
    usuario.delete()
    messages.success(request, 'Usuário excluído com sucesso.')
    return render (request, 'buscarUsuario/buscar_usuario.html', {'usuario': usuario })