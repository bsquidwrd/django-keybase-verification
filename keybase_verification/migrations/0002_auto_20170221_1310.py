# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keybaseverification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keybaseverification',
            name='data',
            field=models.TextField(blank=True, help_text='Get this by visiting http://keybase.io', null=True),
        ),
    ]
