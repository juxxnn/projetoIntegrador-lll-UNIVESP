from django.core.mail import send_mail

def enviar_email_confirmacao(email):
    # Link do formulário do Google Forms
    form_url = 'https://forms.gle/oKLRNdxMHw2wVE4v7'
    # Enviar e-mail de confirmação com o link do formulário do Google Forms
    send_mail(
        'Olá',
        f'Por favor, clique no link abaixo para preencher o formulário:\n\n{form_url}',
        [email],
        fail_silently=False,
    )
