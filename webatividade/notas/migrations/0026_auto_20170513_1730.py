# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0025_auto_20170513_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.Fornecedor'),
        ),
    ]