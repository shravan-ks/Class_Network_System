# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-27 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190426_0027'),
        ('chat', '0007_remove_chat_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='Profile',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.Profile'),
            preserve_default=False,
        ),
    ]