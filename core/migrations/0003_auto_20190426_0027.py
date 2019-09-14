# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-25 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profile_sem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='dept',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
