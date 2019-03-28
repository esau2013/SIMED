from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def cadastro_main(request):
    return render(request, 'cadastro_main.html')

@login_required
def cadastro_par(request):
    return render(request, 'cadastro_par.html')

@login_required
def cadastro_med(request):
    return render(request, 'cadastro_med.html')

@login_required
def atendimento_main(request):
    return render(request, 'atendimento_main.html')

@login_required
def atendimento_nov(request):
    return render(request, 'atendimento_nov.html')

@login_required
def consulta_main(request):
    return render(request, 'consulta_main.html')

@login_required
def ambulatorio_main(request):
    return render(request, 'ambulatorio_main.html')

@login_required
def consulta_par(request):
    return render(request, 'consulta_par.html')

@login_required
def registro_ate(request):
    return render(request, 'registro_ate.html')

@login_required
def registro_exa(request):
    return render(request, 'registro_exa.html')
