# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 14:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20161009_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='test',
        ),
    ]
