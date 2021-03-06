# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-12 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=400)),
                ('CONSUMER_KEY', models.CharField(max_length=400)),
                ('CONSUMER_SECRET', models.CharField(max_length=400)),
                ('ACCESS_KEY', models.CharField(max_length=400)),
                ('ACCESS_SECRET', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=400)),
                ('imageURI', models.CharField(max_length=400)),
                ('popularityIndex', models.CharField(max_length=400)),
            ],
        ),
    ]
