# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-27 09:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_chat_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='Profile',
        ),
    ]
