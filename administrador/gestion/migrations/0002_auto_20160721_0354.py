# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-21 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='codigo',
            field=models.CharField(max_length=8),
        ),
    ]