from django.http import HttpResponse
from .models import Fornecedor, Nota

def listaFornecedor(request):
    html = "<h1>Lista de Fornecedores</h1>"
    listaFornecedor = Fornecedor.objects.all()
    for fornecedor in listaFornecedor:
        html += '<li><strong>{}</strong></li>'.format(fornecedor.nomeFantasia)
        html += '<ul><li>CNPJ: {}</li>'.format(fornecedor.cnpj)
    return HttpResponse(html)

def listaNotas(request):
    html = "<h1>Lista de Notas</h1>"
    listaNota = Nota.objects.all()
    for nota in listaNota:
        html += '<li><strong>{}</strong></li>'.format(nota.fornecedor)
        html += '<ul><li>valor: {}</li>'.format(nota.valor)
    return HttpResponse(html)
