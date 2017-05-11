# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=10, verbose_name='valor')),
            ],
        ),
        migrations.CreateModel(
            name='NotaServico',
            fields=[
                ('nota_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notas.Nota')),
                ('diasServico', models.CharField(max_length=200, verbose_name='diasServico')),
            ],
            bases=('notas.nota',),
        ),
        migrations.AddField(
            model_name='nota',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.Fornecedor'),
        ),
    ]
