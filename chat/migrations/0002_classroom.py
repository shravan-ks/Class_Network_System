# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-25 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(max_length=255)),
                ('dept', models.CharField(max_length=255)),
                ('sub', models.CharField(max_length=255)),
            ],
        ),
    ]
