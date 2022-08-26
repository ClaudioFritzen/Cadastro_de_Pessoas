from django.contrib import admin
from .models import Pessoa, Contato
# Register your models here.

@admin.action(description='Ativar todas as pessoas')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=True)


@admin.action(description='Desativar todos')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativa=False)

class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
        'ativa'
    ]
    list_filter = [
        'ativa',
        'data_nascimento'
    ]
    list_field = [
        'nome_completo'
    ]
    actions = [
        ativar_todos,
        desativar_todos
        
    ]




admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contato)
