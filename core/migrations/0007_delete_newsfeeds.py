# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-05-09 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190510_0143'),
    ]

    operations = [
        migrations.DeleteModel(
            name='newsfeeds',
        ),
    ]