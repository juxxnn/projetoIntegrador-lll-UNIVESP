from django import forms

class SearchForm(forms.Form):
    consulta = forms.CharField(label='consulta')
