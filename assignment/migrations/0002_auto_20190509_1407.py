# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-05-09 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_remove_chat_classinfo'),
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='sem',
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='user',
        ),
        migrations.AddField(
            model_name='assignment',
            name='sub',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chat.classroom'),
            preserve_default=False,
        ),
    ]
