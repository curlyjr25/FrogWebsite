# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surgery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surgery',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
