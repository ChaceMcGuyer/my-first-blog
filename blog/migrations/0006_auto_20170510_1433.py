# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170509_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
