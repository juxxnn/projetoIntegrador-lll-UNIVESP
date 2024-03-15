import os
import json
import requests
from django.shortcuts import render, redirect, get_object_or_404
from criarUsuario.forms import CadUsuarioForm
from setup import settings
from .models import Usuario, CustomUser
from buscarUsuario.views import buscarUsuario
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from datetime import datetime    
from django.core.exceptions import ValidationError


def editarUsuario(request, usuario_id):  
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)

    # data_nascimento (campo tipo 'DateField')
    data_nascimento_valor = usuario.data_nascimento
    data_nascimento_formatado = data_nascimento_valor.strftime('%Y-%m-%d')
    request.session['data_nascimento'] = data_nascimento_formatado

    # data_expedição (campo tipo 'DateField')
    data_expedicao_valor = usuario.data_expedicao
    data_expedicao_formatado = data_expedicao_valor.strftime('%Y-%m-%d')
    request.session['data_expedicao'] = data_expedicao_formatado

    # foto3x4 (campo tipo ImageField)
    foto3x4_nome = usuario.foto3x4.name # Obter o nome do arquivo do ImageField
    request.session['foto3x4'] = foto3x4_nome # Armazena o nome da imagem na variável de sessão

    # rg_usuario (campo tipo FileField)
    rg_usuario_nome = usuario.rg_usuario.name 
    request.session['rg_usuario'] = rg_usuario_nome

    # cert_nasc_usuario (campo tipo FileField)
    cert_nasc_usuario_nome = usuario.cert_nasc_usuario.name 
    request.session['cert_nasc_usuario'] = cert_nasc_usuario_nome

    # rg_responsavel (campo tipo FileField)
    rg_responsavel_nome = usuario.rg_responsavel.name 
    request.session['rg_responsavel'] = rg_responsavel_nome

    # comprov_residencia (campo tipo FileField)
    comprov_residencia_nome = usuario.comprov_residencia.name 
    request.session['comprov_residencia'] = comprov_residencia_nome

    # autorizacao (campo tipo FileField)
    autorizacao_nome = usuario.autorizacao.name 
    request.session['autorizacao'] = autorizacao_nome                

    #Lista de nomes de atributos para atribuir às variáveis ​​de sessão
    atributos = ['id_usuario', 'numero_cadastro', 'eol', 'nome_completo', 'nome_social', 'raca_cor',
                 'cidade', 'uf', 'idade', 'certidao_nascimento', 'folha', 'livro', 'numero_certidao',
                 'rg', 'necessidade_especial', 'nome_completo_responsavel', 'endereco',
                 'endereco_numero', 'complemento', 'cep', 'telefone_residencial', 'telefone_celular',
                 'telefone_recado', 'nome_telefone_recado', 'tipo_sanguineo', 'convenio', 'alergias', 
                 'problemas_saude','tratamento_medico', 'restricao_ativfisica', 'lesao_fratura_cirurgia'
                ]
        
    for atributo in atributos:
        valor = getattr(usuario, atributo)
        if valor == 'disabled':
            valor = ''
        request.session[atributo] = valor

    # Redirecionar para o formulário -> Passo 1
    return redirect('passo_um')



def passo1(request):
    if request.method == 'POST':       
        form_passo1 = request.POST.dict() # Recuperar dados do formulário (Passo 1)        
        request.session.update(form_passo1)# Criar variáveis de sessão
        # Armazenar os valores coletados do formulário (Passo 1) em sessões de variáveis 
        request.session['numero_cadastro'] = form_passo1['numero_cadastro']
        request.session['eol'] = form_passo1['eol']
        request.session['nome_completo'] = form_passo1['nome_completo']
        request.session['nome_social'] = form_passo1['nome_social']
        request.session['raca_cor'] = form_passo1['raca_cor']

        # Formatação do campo 'date' de data_nascimento
        data_nascimento_str = form_passo1['data_nascimento']
        data_nascimento = datetime.strptime(data_nascimento_str,'%Y-%m-%d')
        data_nascimento_formatado = data_nascimento.strftime('%Y-%m-%d')  
        request.session['data_nascimento'] = data_nascimento_formatado # Atribuir a data formatada à variável de sessão

        request.session['idade'] = form_passo1['idade']
        request.session['certidao_nascimento'] = form_passo1['certidao_nascimento']
        request.session['folha'] = form_passo1['folha']
        request.session['livro'] = form_passo1['livro']
        request.session['numero_certidao'] = form_passo1['numero_certidao']
        request.session['rg'] = form_passo1['rg']

        # Formatação do campo 'date' da 'data_expedicao'
        data_expedicao_str = form_passo1['data_expedicao']
        data_expedicao = datetime.strptime(data_expedicao_str,'%Y-%m-%d')
        data_expedicao_formatado = data_expedicao.strftime('%Y-%m-%d')  
        request.session['data_expedicao'] = data_expedicao_formatado # Atribuir a data formatada à variável de sessão

        request.session['necessidade_especial'] = form_passo1['necessidade_especial']                        
        request.session['nome_completo_responsavel'] = form_passo1['nome_completo_responsavel']

        # Redirecionar para o formulário -> Passo 2
        return redirect('passo_dois')
    else:
        return render(request,'criarUsuario/passo1_dadospessoais.html')

def passo2(request):
    if request.method == 'POST':        
        form_passo2 = request.POST.dict() # Recuperar dados do formulário (Passo 2)        
        request.session.update(form_passo2) # Criar variáveis de sessão
        # Armazenar os valores coletados do formulário (Passo 2) em sessões de variáveis
        request.session['cep'] = form_passo2['cep']
        request.session['endereco_numero'] = form_passo2['endereco_numero']
        request.session['complemento'] = form_passo2['complemento']
        request.session['telefone_residencial'] = form_passo2['telefone_residencial']
        request.session['telefone_celular'] = form_passo2['telefone_celular']
        request.session['telefone_recado'] = form_passo2['telefone_recado']
        request.session['nome_telefone_recado'] = form_passo2['nome_telefone_recado']

        # Redirecionar para o formulário -> Passo 3
        return redirect('passo_tres')
    else:
        return render(request,'criarUsuario/passo2_endereco.html')
    

def buscar_endereco(request):
    if request.method == 'GET':
        cep = request.GET.get('cep', '')
        if cep:
            url = f'https://viacep.com.br/ws/{cep}/json/'
            response = requests.get(url)
            if response.status_code == 200:
                data = json.loads(response.text)
                if not data.get('erro'):
                    endereco = data.get('logradouro', '')
                    uf = data.get('uf', '')
                    localidade = data.get('localidade', '')
                    # Atualizar variáveis de sessão
                    request.session['endereco'] = endereco
                    request.session['cidade'] = localidade
                    request.session['uf'] = uf
                    return JsonResponse({'endereco': endereco})
        return JsonResponse({'erro': 'CEP inválido ou não encontrado'}, status=400)

def passo3(request):
    if request.method== 'POST':        
        form_passo3 = request.POST.dict() # Recuperar dados do formulário (Passo 3)        
        request.session.update(form_passo3) # Criar variáveis de sessão
       # Armazenar os valores coletados do formulário (Passo 3) em sessões de variáveis
        request.session['tipo_sanguineo'] = form_passo3['tipo_sanguineo']
        request.session['convenio'] = form_passo3['convenio']
        request.session['alergias'] = form_passo3['alergias']
        request.session['problemas_saude'] = form_passo3['problemas_saude']
        request.session['tratamento_medico'] = form_passo3['tratamento_medico']
        request.session['restricao_ativfisica'] = form_passo3['restricao_ativfisica']
        request.session['lesao_fratura_cirurgia'] = form_passo3['lesao_fratura_cirurgia']                                            
        # Redirecionar para o formulário -> Passo 4
        return redirect('passo_quatro')
    else:
        return render(request,'criarUsuario/passo3_dadosmedicos.html')

def passo4(request):
    if request.method == 'POST':
        form = CadUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            # Obter a variável de sessão 'eol'
            prefix = request.session.get('eol', '')

            # Armazenar os caminhos dos arquivos em variáveis de sessão
            request.session['foto3x4'] = store_file(request.FILES['foto3x4'], prefix)
            request.session['rg_usuario'] = store_file(request.FILES['rg_usuario'], prefix)
            request.session['cert_nasc_usuario'] = store_file(request.FILES['cert_nasc_usuario'], prefix)
            request.session['rg_responsavel'] = store_file(request.FILES['rg_responsavel'], prefix)
            request.session['comprov_residencia'] = store_file(request.FILES['comprov_residencia'], prefix)
            request.session['autorizacao'] = store_file(request.FILES['autorizacao'], prefix)

            #---------- Salvando Passo1, Passo 2, Passo 3 e Passo 4 ----------# 
            # id do funcionário que está logado (chave estrangeira)
            func_id = request.session['sessao_func_id'] 
            funcionario = CustomUser.objects.get(idfunc=func_id)

            # Salvar os dados da sessão na base de dados
            dados_do_usuario = Usuario(
                #----- Passo 1 -----#
                idfunc = funcionario, #funcionário logado durante o cadastramento 
                numero_cadastro = request.session['numero_cadastro'],
                eol = request.session['eol'],
                nome_completo = request.session['nome_completo'],
                nome_social = request.session['nome_social'],
                raca_cor = request.session['raca_cor'],
                cidade = request.session['cidade'],
                uf = request.session['uf'],
                data_nascimento = request.session['data_nascimento'],
                idade = request.session['idade'],
                certidao_nascimento = request.session['certidao_nascimento'],
                folha = request.session['folha'],
                livro = request.session['livro'],
                numero_certidao = request.session['numero_certidao'],
                rg = request.session['rg'],
                data_expedicao = request.session['data_expedicao'],
                necessidade_especial = request.session['necessidade_especial'],
                nome_completo_responsavel = request.session['nome_completo_responsavel'],
                #----- Passo 2 -----# 
                endereco = request.session['endereco'], 
                endereco_numero = request.session['endereco_numero'],
                complemento = request.session['complemento'],
                cep = request.session['cep'],
                telefone_residencial = request.session['telefone_residencial'],
                telefone_celular = request.session['telefone_celular'],
                telefone_recado = request.session['telefone_recado'],
                nome_telefone_recado = request.session['nome_telefone_recado'], 
                #----- Passo 3 -----#
                tipo_sanguineo = request.session['tipo_sanguineo'], 
                convenio = request.session['convenio'], 
                alergias = request.session['alergias'],
                problemas_saude = request.session['problemas_saude'],
                tratamento_medico = request.session['tratamento_medico'],
                restricao_ativfisica = request.session['restricao_ativfisica'],
                lesao_fratura_cirurgia = request.session['lesao_fratura_cirurgia'],
                #----- Passo 4 -----#
                foto3x4 = request.session['foto3x4'],
                rg_usuario = request.session['rg_usuario'],
                cert_nasc_usuario = request.session['cert_nasc_usuario'],
                rg_responsavel = request.session['rg_responsavel'],
                comprov_residencia = request.session['comprov_residencia'],
                autorizacao = request.session['autorizacao']
            )

            # Decidindo se atualizo ou insiro os dados do usuário em razão da presença do id_usuario nas variáveis de sessão
            if 'id_usuario' in request.session:
                dados_do_usuario.id_usuario = request.session['id_usuario']
                dados_do_usuario.save() # Update
                messages.success(request, "Os dados do usuário foram atualizados com sucesso!")            
            else:                      
                dados_do_usuario.save() # Insert
                messages.success(request, "O usuário foi cadastrado com sucesso!")

            #----- Apagar o conteúdo das variáveis de sessão, exceto as do funcionário logado -----#
            # Identificar quais são as variáveis de sessão do funcionário logado
            variaveis_sessao_funcionario = ['email', 'password', 'sessao_func_id']

            # Iterar sobre as variáveis de sessão
            for key in list(request.session.keys()):
                if key not in variaveis_sessao_funcionario:
                    del request.session[key]

            # Salvar a modificação da sessão
            request.session.modified = True

            return render (request,'criarUsuario/passo1_dadospessoais.html')
        else:
            return render (request,'criarUsuario/passo4_enviardocumentos.html')
    else:
        return render (request,'criarUsuario/passo4_enviardocumentos.html')

# Método para alterar o nome da imagem ou do pdf e determinar o caminho de armazenamento
# Verify the existence of a file with the same name in path. If there is, delete it.
# Inside the with open(filepath, 'wb+') as destination: block, the file is opened in write-binary mode ('wb+')
# to ensure that binary files like images or PDFs are correctly handled.
# Using a loop, the file is read in chunks from the input file object (file) and written to the destination file
# (destination) in the specified file path.
# Finally, the filepath is returned, allowing you to retrieve the file path and store it in session variables or
# perform other operations as needed.
def store_file(file, prefix):
    filename = f"{prefix}_{file.name}" # Adicionar o prefixo ao nome do arquivo
    filepath = os.path.join(settings.MEDIA_ROOT, filename) # Determinar o caminho do arquivo

    # Verificar se o arquivo já existe
    if os.path.exists(filepath):
        os.remove(filepath)  # Apagar o arquivo existente

    with open(filepath, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return filepath