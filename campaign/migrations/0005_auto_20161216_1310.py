# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0004_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='post1',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='post2',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='post3',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='post4',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='post5',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='post6',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='post7',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='post8',
        ),
        migrations.AddField(
            model_name='campaign',
            name='campaign_name',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='campaign',
            name='campaign_sequence',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='campaign',
            name='owner',
            field=models.CharField(default='admin', max_length=20),
        ),
        migrations.AddField(
            model_name='campaign',
            name='participants',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='campaign',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('P', 'Paused'), ('I', 'Inactive')], default='I', max_length=1),
        ),
        migrations.AddField(
            model_name='campaign',
            name='visits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
