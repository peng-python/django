# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-09 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='receive_name',
            field=models.CharField(default='', max_length=20, verbose_name='\u6536\u8d27\u4eba\u59d3\u540d'),
        ),
    ]
