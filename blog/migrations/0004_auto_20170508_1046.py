# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170508_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
