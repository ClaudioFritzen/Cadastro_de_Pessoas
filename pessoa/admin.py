from django.contrib import admin
from .models import Pessoa, Contato
# Register your models here.

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

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contato)
