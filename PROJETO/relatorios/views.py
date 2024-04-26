from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def relatorios(request):
    return render(request, 'relatorios/relatorio.html')

@login_required
def dashboard_template_view(request):
    return relatorios(request)