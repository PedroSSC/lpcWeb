from django.http import HttpResponse
from .models import Fornecedor, Nota, NotaServico, NotaVenda

def index(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/fornecedores'>Fornecedor</a></li>
                    <li><a href='/notas'>Nota</a></li>
                    <ul>
                        <li><a href='/servico'>Notas de Serviço</a></li>
                        <li><a href='/venda'>Notas de Venda</a></li>
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
        html += '<li><strong>{}</strong></li>'.format(nota.fornecedor.nomeFantasia)
        html += '<ul><li>valor: {}</li></ul>'.format(nota.valor)
    return HttpResponse(html)

def listaServico(request):
    html = "<h1>Lista de Notas de Serviço</h1>"
    listaNotasServico = NotaServico.objects.all()
    for notasserv in listaNotasServico:
        html += '<li><strong>{}</strong></li>'.format(notasserv.fornecedor.nomeFantasia)
        html += '<ul><li>valor: {}</li>'.format(notasserv.valor)
        html += '<li>dias de serviço: {}</li></ul>'.format(notasserv.diasServico)
    return HttpResponse(html)

def listaVenda(request):
    html = "<h1>Lista de Notas de Venda</h1>"
    listaNotasVenda = NotaVenda.objects.all()
    for notavenda in listaNotasVenda:
        html += '<li><strong>{}</strong></li>'.format(notavenda.fornecedor.nomeFantasia)
        html += '<ul><li>valor: {}</li>'.format(notavenda.valor)
        html += '<li>dias de serviço: {}</li></ul>'.format(notavenda.diasServico)
    return HttpResponse(html)
