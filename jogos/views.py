from django.shortcuts import render
from .models import Modalidade, Tecnico, Equipe, Atleta
# Create your views here.

def IndexViews(request):
    equipe = Equipe.objects.all()
    modalidade = Modalidade.objects.all()
    context = {
        'equipe': equipe,
        'modalidade': modalidade
    }
    return render(request, 'index.html', context)

def EquipeViews(request, equipe_id):
    equipe = Equipe.objects.get(id=equipe_id)
    atletas = Atleta.objects.filter(equipe=equipe)
    context = {
        'equipe': equipe
    }
    return render(request, 'equipe.html', context)

def ModalidadeViews(request, modalidade_id):
    modalidade = Modalidade.objects.get(id=modalidade_id)
    atleta = Atleta.objects.filter(modalidade=modalidade)
    context = {
        'modalidade': modalidade,
        'atleta': atleta
    }
    return render(request, 'modalidade.html', context)