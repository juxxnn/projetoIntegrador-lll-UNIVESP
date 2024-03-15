from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from criarConta.models import CustomUser

def signin(request): 
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():            
            email = form.cleaned_data['email']
            senha = form.cleaned_data["senha"]

            # A função authenticate retorna o objeto 'user' autenticado se as credenciais forem válidas, mas não cria a sessão do 'user'
            user = authenticate(request, email=email, password=senha)            

            if user is not None:
            # A função login é responsável por criar a sessão do usuário e requer o objeto 'user' autenticado como argumento.
                login(request, user)
                # Se sessao_func_id não existir, ela será criada e receberá o valor idfunc (variáveis de sessão com prefixo: sessao)      
                request.session['sessao_func_id'] = user.idfunc              
                return redirect('logado')
            else:
                messages.error(request, 'Email e/ou senha incorretos.')

    else:
        form = LoginForm()
        
    return render(request, 'login/login.html', {'form': form})

def logado(request):
    return render(request, 'buscarUsuario/buscar_usuario.html')
    #return render(request, 'alterarConta/alterar_conta.html')
    #return render(request, 'login/login.html')

def deslogado(request):
    request.session.flush()
    logout(request)
    # Redirecionar para uma URL específica após deslogar
    return redirect('/')

