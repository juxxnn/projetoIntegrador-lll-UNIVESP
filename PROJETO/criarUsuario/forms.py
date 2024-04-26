from django import forms
from .models import Usuario
from django.core.exceptions import ValidationError

class CadUsuarioForm(forms.ModelForm):
    MAX_IMAGE_SIZE = 1 * 1024 * 1024  # 1MB
    MAX_PDF_SIZE = 3 * 1024 * 1024  # 3MB

    def clean_foto3x4(self):
        foto3x4 = self.cleaned_data.get('foto3x4')
        if foto3x4:
            if not foto3x4.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError('Apenas imagens JPG, JPEG e PNG são permitidas.')
            if foto3x4.size > self.MAX_IMAGE_SIZE:
                raise ValidationError(f'O tamanho máximo da imagem é {self.MAX_IMAGE_SIZE} bytes.')
        return foto3x4

    def clean_rg_usuario(self):
        return self.clean_pdf_field('rg_usuario')

    def clean_cert_nasc_usuario(self):
        return self.clean_pdf_field('cert_nasc_usuario')

    def clean_rg_responsavel(self):
        return self.clean_pdf_field('rg_responsavel')

    def clean_comprov_residencia(self):
        return self.clean_pdf_field('comprov_residencia')

    def clean_autorizacao(self):
        return self.clean_pdf_field('autorizacao')

    def clean_pdf_field(self, field_name):
        pdf = self.cleaned_data.get(field_name)
        if pdf:
            if not pdf.name.lower().endswith('.pdf'):
                raise ValidationError('Apenas documentos PDF são permitidos.')
            if pdf.size > self.MAX_PDF_SIZE:
                raise ValidationError(f'O tamanho máximo do documento PDF é {self.MAX_PDF_SIZE} bytes.')
        return pdf

    class Meta:
        model = Usuario
        fields = [ 
            'numero_cadastro',
            'eol',
            'nome_completo',
            'nome_social',
            'raca_cor',
            'cidade',
            'uf',
            'data_nascimento',
            'idade',
            'certidao_nascimento',
            'folha',
            'livro',
            'numero_certidao',
            'rg',
            'data_expedicao',
            'e_mail',
            'necessidade_especial',
            'nome_completo_responsavel',
            'endereco',
            'endereco_numero',
            'complemento',
            'cep',
            'telefone_residencial',
            'telefone_celular',
            'telefone_recado',
            'nome_telefone_recado',
            'tipo_sanguineo',
            'convenio',
            'alergias',
            'problemas_saude',
            'tratamento_medico',
            'restricao_ativfisica',
            'lesao_fratura_cirurgia',
            'foto3x4',
            'rg_usuario',
            'cert_nasc_usuario',
            'rg_responsavel',
            'comprov_residencia',
            'autorizacao',
        ]