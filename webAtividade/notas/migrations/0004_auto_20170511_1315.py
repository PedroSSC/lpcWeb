# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-11 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0003_auto_20170511_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notas.Fornecedor'),
        ),
    ]