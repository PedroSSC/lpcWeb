# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 03:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0022_auto_20170512_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notacompra',
            name='nota_ptr',
        ),
        migrations.AlterField(
            model_name='nota',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.Fornecedor'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='valor',
            field=models.CharField(max_length=10, verbose_name='valor'),
        ),
        migrations.DeleteModel(
            name='NotaCompra',
        ),
    ]
