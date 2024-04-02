from django.core.mail import send_mail
from django.conf import settings

def enviar_email_confirmacao(e_mail):

    # Link do formulário do Google Forms
    form_url = 'https://forms.gle/oKLRNdxMHw2wVE4v7'

    # Lista de destinatários do e-mail
    recipient_list = [e_mail]

    # Conteúdo HTML do e-mail
    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                font-size: 14px;
                color: black;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }}
            .header {{
                background-color: #007bff;
                color: #fff;
                padding: 10px;
                text-align: center;
            }}
            .content {{
                padding: 20px;
                background-color: #f9f9f9;
                border-radius: 5px;
            }}
            .button {{
                background-color: #A2B5CD;
                color: #FFFFFF;
                text-decoration: none;
                padding: 10px 20px;
                border-radius: 3px;
                display: inline-block;
                font-weight: bold;
                text-align: center;

            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>CEU Parque Bristol</h2>
            </div>
            <div class="content">
                <p>Olá,</p>
                <p>Estamos conduzindo uma pesquisa para entender melhor a comunidade do CEU Parque Bristol e suas necessidades. Gostaríamos de contar com a sua colaboração!</p>
                <p>Por favor, clique no botão abaixo para acessar o formulário de pesquisa e compartilhar suas opiniões conosco:</p>
                <a class="button" href="{form_url}">Preencher Formulário</a>
                <p>O formulário é simples e levará apenas alguns minutos para ser preenchido. Suas respostas são extremamente valiosas para nós e nos ajudarão a melhorar nossos serviços e atividades no CEU.</p>
                <p>Agradecemos antecipadamente pela sua participação!</p>
            </div>
        </div>
    </body>
    </html>
"""

    # Enviar e-mail de confirmação com o link do formulário do Google Forms
    send_mail(
        subject='Participe da nossa pesquisa no CEU Parque Bristol!',
        message='',  # Deixe a mensagem vazia para enviar apenas o conteúdo HTML
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[e_mail],
        html_message=html_content,  # Passando o conteúdo HTML como parte da mensagem
        fail_silently=False,
    )
