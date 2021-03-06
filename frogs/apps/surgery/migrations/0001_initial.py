# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 01:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surgery_number', models.IntegerField()),
                ('date', models.DateField()),
                ('frog', models.CharField(max_length=200)),
                ('tank_number', models.IntegerField()),
                ('collagenase', models.IntegerField()),
                ('collagenase_amount', models.IntegerField()),
                ('activity', models.IntegerField()),
                ('solution_volume', models.IntegerField()),
                ('g_b_oocytes', models.CharField(max_length=1)),
                ('company', models.CharField(max_length=200)),
                ('number_oocytes_ordered', models.IntegerField()),
                ('complaints', models.BooleanField()),
                ('notes', models.TextField()),
                ('previous_surgery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surgery.Surgery')),
            ],
        ),
    ]
