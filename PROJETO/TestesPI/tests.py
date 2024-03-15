from django.test import TestCase
from django.urls import reverse
from criarConta.models import CustomUser

class SigninViewTest(TestCase):
    def setUp(self):
        # Criando um usuário para o teste
        self.user = CustomUser.objects.create_user(
            email='usuario@example.com',
            registro_funcional='123456',
            nome_completo='Nome do Usuário',
            password='senha123'
        )

    def test_login_mal_sucedido(self):
        # Fazendo uma requisição POST com credenciais incorretas
        response = self.client.post(reverse('login_funcionario'), {'email': 'usuario@example.com', 'senha': 'senha_errada'})
        
        # Verificando se a página de login foi exibida novamente
        self.assertEqual(response.status_code, 200)
        
        # Verificando se a mensagem de erro está presente no contexto
        self.assertContains(response, 'Email e/ou senha incorretos.')
        print("Email e/ou senha incorretos.")