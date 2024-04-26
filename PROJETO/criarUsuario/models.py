from django.db import models
from criarConta.models import CustomUser

class Usuario(models.Model):
    # Passo 1
    id_usuario = models.AutoField(primary_key=True) # chave primária
    idfunc = models.ForeignKey(CustomUser, on_delete=models.PROTECT, editable=False) #chave estrangeira (id do funcionário)     
    numero_cadastro= models.IntegerField(null=True, blank=True, default=None)
    eol = models.IntegerField(null=True, blank=True, default=None)
    nome_completo = models.CharField(max_length=100, null=True, blank=True)
    nome_social = models.CharField(max_length=100, null=True, blank=True)
    raca_cor = models.CharField(max_length=20, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    uf = models.CharField(max_length=2, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    idade = models.PositiveSmallIntegerField(null=True, blank=True, default=None)
    certidao_nascimento = models.CharField(max_length=10, null=True, blank=True)
    folha = models.CharField(max_length=10, null=True, blank=True)
    livro = models.CharField(max_length=10, null=True, blank=True)
    numero_certidao = models.CharField(max_length=25, null=True, blank=True)
    rg = models.CharField(max_length=27, null=True, blank=True)
    data_expedicao = models.DateField(null=True, blank=True)
    e_mail = models.CharField(max_length=100, null=True, blank=True)
    necessidade_especial =  models.CharField(max_length=255, null=True, blank=True)
    nome_completo_responsavel = models.CharField(max_length=100, null=True, blank=True)
    # Passo 2
    endereco = models.CharField(max_length=100, null=True, blank=True)    
    endereco_numero = models.CharField(max_length=10, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    telefone_residencial = models.CharField(max_length=15, null=True, blank=True)
    telefone_celular = models.CharField(max_length=15, null=True, blank=True)
    telefone_recado= models.CharField(max_length=15, null=True, blank=True)
    nome_telefone_recado = models.CharField(max_length=100, null=True, blank=True)
    # Passo 3
    tipo_sanguineo = models.CharField(max_length=10, null=True, blank=True)
    convenio = models.CharField(max_length=100, null=True, blank=True)
    alergias = models.CharField(max_length=100, null=True, blank=True)
    problemas_saude = models.CharField(max_length=100, null=True, blank=True)
    tratamento_medico = models.CharField(max_length=100, null=True, blank=True)    
    restricao_ativfisica = models.CharField(max_length=100, null=True, blank=True)    
    lesao_fratura_cirurgia = models.CharField(max_length=100, null=True, blank=True)    
    # Passo 4
    foto3x4 = models.ImageField(upload_to='documentos/', blank=True) # imagem jpg, jpeg ou png
    rg_usuario = models.FileField(upload_to = 'documentos/', blank=True) # documento pdf
    cert_nasc_usuario = models.FileField(upload_to = 'documentos/', blank=True) # documento pdf
    rg_responsavel = models.FileField(upload_to = 'documentos/', blank=True) # documento pdf
    comprov_residencia = models.FileField(upload_to = 'documentos/', blank=True) # documento pdf
    autorizacao = models.FileField(upload_to = 'documentos/', blank=True) # documento pdf    