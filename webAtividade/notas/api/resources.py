from tastypie.resources import ModelResource
from notas.models import *
from django.contrib.auth.models import User
from tastypie.authorization import Authorization


class FornecedorResource(ModelResource):
    class Meta:
        queryset = Fornecedor.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
        filtering = {
            "nomeFantasia": ('exact', 'startswith',)
        }
"""
    A api está funcionando para o get e post, o put não funciona
e o delete apaga todos os registros.

URI para apresentar o resource de fornecedor em Json:
http://127.0.0.1:8000/api/v1/fornecedor/

Exemplo de payload para usar com o Advanced Rest Client:
{"nomeFantasia":"teste1"}

"""
