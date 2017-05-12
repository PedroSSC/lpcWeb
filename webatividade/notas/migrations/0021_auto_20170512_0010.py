# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 03:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0020_auto_20170512_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notacompra',
            name='valorProdutos',
        ),
        migrations.RemoveField(
            model_name='notaservico',
            name='valorDiaria',
        ),
        migrations.AddField(
            model_name='nota',
            name='valor',
            field=models.CharField(default=0, max_length=10, verbose_name='valor'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.Fornecedor'),
        ),
        migrations.AlterField(
            model_name='notacompra',
            name='qtProd',
            field=models.CharField(max_length=10, verbose_name='qtProd'),
        ),
        migrations.AlterField(
            model_name='notaservico',
            name='diasServico',
            field=models.CharField(max_length=200, verbose_name='diasServico'),
        ),
    ]