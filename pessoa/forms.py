from dataclasses import fields
from django.forms import ModelForm, fields, models
from django import forms
from .models import Pessoa

class PessoaForm(ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    class Meta:
        model = Pessoa
        fields = ['nome_completo',  'data_nascimento', 'ativa']
        # fields = ['__all__']