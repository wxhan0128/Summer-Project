# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-23 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='chef_experience',
            field=models.CharField(blank=True, choices=[('a', 'a'), ('b', 'b'), ('c', 'c')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='chef_type',
            field=models.CharField(blank=True, choices=[('newbie', 'newbie'), ('professional', 'professional'), ('other', 'other')], max_length=20, null=True),
        ),
    ]