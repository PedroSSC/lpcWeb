from django.http import HttpResponse
from .models import Fornecedor, Nota

def index(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/fornecedores'>Fornecedor</a></li>
                    <li><a href='/notas'>Nota</a></li>
                    <ul>
                        <li><a href='/NotaServico'>Notas de Serviço</a></li>
                        <li><a href='/NotaVenda'>Notas de Venda</a></li>
                    </ul>
                </ul>
            """
    return HttpResponse(html)

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
