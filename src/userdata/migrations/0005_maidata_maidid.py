# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-05 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0004_maidata'),
    ]

    operations = [
        migrations.AddField(
            model_name='maidata',
            name='maidid',
            field=models.CharField(max_length=5, null=True),
        ),
    ]