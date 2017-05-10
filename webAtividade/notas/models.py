from django.db import models
from django.utils import timezone


class Fornecedor(models.Model):
    nomeFantasia = models.CharField('nomeFantasia', max_length=200)
    cnpj = models.CharField('cnpj', max_length=100)
