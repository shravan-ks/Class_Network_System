# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-27 08:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_chat_sec'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='sec',
        ),
    ]
