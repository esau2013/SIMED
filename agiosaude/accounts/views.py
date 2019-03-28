from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import EditHospitalForm
from agiosaude.core.models import *
from agiosaude.accounts.models import User
from django.contrib import messages

# Create your views here.
@login_required
def Usuario_Main(request):
    usuarios = User.objects.all()
    template_name = 'usuario_main.html'
    context ={'usuarios':usuarios}
    return render()

@login_required
def usuario_nov(request):
    return render(request, 'usuario_nov.html')

@login_required
def edit(request):
    obj = get_object_or_404(Hospital, pk=1)
    template_name = 'hospital.html'
    context = {}
    if request.method == 'POST':
        form = EditHospitalForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Os dados foram atualizados com sucesso!')
            return redirect('core:home')
    else:
        form = EditHospitalForm(instance=obj)
    context['form'] = form
    return render(request, template_name, context)
