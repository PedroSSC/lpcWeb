from tastypie.resources import ModelResource
from tastypie import fields, utils
from notas.models import Fornecedor
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
