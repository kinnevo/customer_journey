# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 01:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0002_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='user_id',
            new_name='username',
        ),
    ]
