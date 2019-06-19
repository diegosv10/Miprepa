# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('badges', '0002_auto_20160526_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='min_quantity_challenge',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad mínima por Reto'),
        ),
        migrations.AlterField(
            model_name='badge',
            name='type',
            field=models.CharField(blank=True, choices=[('practice', 'Práctica'), ('survival', 'Sobreviviente'), ('miscellany', 'Miscelánea')], max_length=10, null=True),
        ),
    ]
