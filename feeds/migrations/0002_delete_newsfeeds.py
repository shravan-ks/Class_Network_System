# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-05-10 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='newsfeeds',
        ),
    ]