# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-23 01:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.TextField(blank=True, max_length=255, null=True)),
                ('chef_type', models.CharField(blank=True, choices=[('newbie', 'newbie'), ('professional', 'professional'), ('other', 'other')], max_length=60, null=True)),
                ('chef_experience', models.CharField(blank=True, choices=[('a', 'a'), ('b', 'b'), ('c', 'c')], max_length=60, null=True)),
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
