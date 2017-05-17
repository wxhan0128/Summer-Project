# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-16 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170516_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=55, verbose_name='Name of User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='short_description',
            field=models.TextField(blank=True, max_length=500, verbose_name='Brief Introduction'),
        ),
    ]