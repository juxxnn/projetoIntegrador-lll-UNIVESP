from django.contrib import messages
from django.shortcuts import render, redirect
from criarConta.models import CustomUser
from .forms import RegistrationForm

def criarConta(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registro_funcional = form.cleaned_data['registro_funcional']
            email = form.cleaned_data['email'] 
            senha1 = form.cleaned_data['senha1']
            senha2 = form.cleaned_data['senha2']                       
            error_messages = []
            
            if CustomUser.objects.filter(registro_funcional=registro_funcional).exists():          
                error_messages.append('O registro funcional já foi usado.')

            if CustomUser.objects.filter(email__iexact=email).exists():
                error_messages.append('O email digitado já foi usado.') 

            if senha1 != senha2:                
                error_messages.append('As senhas não coincidem.')                

            if error_messages:
                error_message = '<br>'.join(error_messages)
                messages.error(request, error_message)            
            else:
                user = form.save()            
                return redirect('sucesso')
    else:
        form = RegistrationForm()
    return render(request, 'criarConta/criar_conta.html', {'form': form})    
    
def sucesso(request):
    return render(request, 'criarConta/sucesso.html')