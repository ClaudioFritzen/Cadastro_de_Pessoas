from django.shortcuts import render
from django.http import Http404, HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . models import Pessoa, Contato 
from .forms import PessoaForm

# Create your views here.

class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('buscarNome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)

        return queryset

class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    #url de sucesso para 
    success_url = '/pessoas/'

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'

class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'
    


#criando contato
def contatos(request, pk_pessoa):
    contatos = Contato.objects.filter(pessoa = pk_pessoa)
    return render(request, 'contato/contato_list.html', {'contatos': contatos})


