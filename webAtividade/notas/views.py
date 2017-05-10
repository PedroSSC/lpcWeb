from django.shortcuts import render
from django.http import HttpResponse
from .models import Fornecedor

def listaFornecedor(request):
    html = "<h1>Lista de Fornecedores</h1>"
    listaFornecedor = Fornecedor.objects.all()
    for fornecedor in listaFornecedor:
        html += '<li><strong>{}</strong></li>'.format(Fornecedor.nomeFantasia)
        html += '<ul><li>CNPJ: {}</li>'.format(Fornecedor.cnpj)
    return HttpResponse(html)
