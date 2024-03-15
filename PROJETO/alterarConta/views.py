from django.shortcuts import render, get_object_or_404
from criarConta.models import CustomUser
from django.contrib import messages

def alterarConta(request, func_id):
    funcionario = get_object_or_404(CustomUser, idfunc=func_id)
    return render(request, 'alterarConta/alterar_conta.html', {'funcionario': funcionario})

def salvaAltera(request, func_id):
    funcionario = get_object_or_404(CustomUser, idfunc=func_id)

    if request.method == 'POST':
        novasenha1 = request.POST.get('senha1')
        novasenha2 = request.POST.get('senha2')

        if novasenha1 == novasenha2:
            # Usar o método set_password() no funcionario (que é o do tipo CustomUser) para que o hashing e a encriptação ocorram
            funcionario.set_password(novasenha2)
            funcionario.save()
            messages.success(request, "A sua senha foi atualizada com sucesso!")                     
        else:
            messages.error(request, 'As senhas não coincidem! Digite-as novamente.')        
        
    return render(request, 'alterarConta/alterar_conta.html', {'funcionario': funcionario})