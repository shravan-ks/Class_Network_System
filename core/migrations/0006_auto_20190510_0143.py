# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-05-09 20:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_feeds'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='feeds',
            new_name='newsfeeds',
        ),
    ]