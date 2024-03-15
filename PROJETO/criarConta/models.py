from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, registro_funcional, nome_completo, password=None):
        email = self.normalize_email(email)
        user = self.model(email=email, registro_funcional=registro_funcional, nome_completo=nome_completo)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, registro_funcional, nome_completo, password=None):
        user = self.create_user(email, registro_funcional, nome_completo, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    idfunc = models.AutoField(primary_key=True) #chave primária
    email = models.EmailField(unique=True)
    registro_funcional = models.CharField(max_length=10, null=False, blank=False) #registro funcional
    nome_completo = models.CharField(max_length=100, null=False, blank=False) #nome
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
 
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='customuser_set')    

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for the user.',
        related_name='custom_user_set'  # Unique related_name for CustomUser model
    )

    username = None # username é definido como None, o Django apaga a coluna da base de dados quando 'migrations' é aplicado
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['registro_funcional', 'nome_completo']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    


