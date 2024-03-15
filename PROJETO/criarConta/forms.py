from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    senha1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email', 'registro_funcional', 'nome_completo')

    def clean_password2(self):
        senha1 = self.cleaned_data.get('senha1')
        senha2 = self.cleaned_data.get('senha2')
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError("As senhas não coincidem.")
        return senha2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['senha1'])
        if commit:
            user.save()
        return user