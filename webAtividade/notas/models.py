from django.db import models
from django.utils import timezone


class Fornecedor(models.Model):
    nomeFantasia = models.CharField('nomeFantasia', max_length=200)
    cnpj = models.CharField('cnpj', max_length=100)
    def __repr__(self):
        return self.nomeFantasia

class Nota(models.Model):
    fornecedor = models.ForeignKey('Fornecedor')
    valor = models.CharField('valor', max_length=10)
    def __repr__(self):
        return '{}'.format(self.valor)

class NotaServico(Nota):
    diasServico = models.CharField('diasServico', max_length=200)
    def __repr__(self):
        return '{}'.format(self.diasServico)
