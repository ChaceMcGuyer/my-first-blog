# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
