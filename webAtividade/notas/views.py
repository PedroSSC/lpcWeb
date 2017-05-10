from django.http import HttpResponse
from .models import Fornecedor

def listaFornecedor(request):
    html = "<h1>Lista de Fornecedores</h1>"
    listaFornecedor = Fornecedor.objects.all()
    for fornecedor in listaFornecedor:
        html += '<li><strong>{}</strong></li>'.format(fornecedor.nomeFantasia)
        html += '<ul><li>CNPJ: {}</li>'.format(fornecedor.cnpj)
    return HttpResponse(html)
