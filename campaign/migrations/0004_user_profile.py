# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 19:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaign', '0003_auto_20161214_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_campaign', models.IntegerField(default=0)),
                ('current_sequence', models.IntegerField(default=0)),
                ('priority1', models.IntegerField(default=0)),
                ('priority2', models.IntegerField(default=0)),
                ('priority3', models.IntegerField(default=0)),
                ('priority4', models.IntegerField(default=0)),
                ('priority5', models.IntegerField(default=0)),
                ('priority6', models.IntegerField(default=0)),
                ('priority7', models.IntegerField(default=0)),
                ('priority8', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
