# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_students_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='class_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reports.Class'),
            preserve_default=False,
        ),
    ]
