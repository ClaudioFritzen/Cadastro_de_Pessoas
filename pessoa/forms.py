from dataclasses import fields
from django.forms import ModelForm
from .models import Pessoa

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome_completo',  'data_nascimento', 'ativa']
        # fields = ['__all__']