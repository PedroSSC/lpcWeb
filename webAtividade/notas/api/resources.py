from tastypie.resources import ModelResource
from notas.models import *
from tastypie import fields, utils
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

class NotaResource(ModelResource):
    class Meta:
        fornecedor = fields.ToOneField(FornecedorResource, 'id')
        queryset = Nota.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()

class NotaServicoResource(ModelResource):
    class Meta:
        nota = fields.ToOneField(NotaResource, 'id')
        queryset = NotaServico.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()

class NotaVendaResource(ModelResource):
    class Meta:
        nota = fields.ToOneField(NotaResource, 'id')
        queryset =  NotaVenda.objects.all()
        allowed_methods = ['get','post','delete','put']
        authorization = Authorization()
