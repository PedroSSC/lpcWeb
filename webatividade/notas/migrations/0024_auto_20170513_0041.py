# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 03:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0023_auto_20170513_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotaVenda',
            fields=[
                ('nota_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notas.Nota')),
                ('qtProdutos', models.CharField(max_length=200, verbose_name='qtProdutos')),
            ],
            bases=('notas.nota',),
        ),
        migrations.AlterField(
            model_name='nota',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.Fornecedor'),
        ),
    ]