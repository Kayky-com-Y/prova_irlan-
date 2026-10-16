from django.contrib import admin
from .models import Modalidade, Tecnico, Equipe, Atleta
# Register your models here.

@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'curso']

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'equipe']