# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 04:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0010_auto_20161015_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='birth_Date',
            field=models.DateField(verbose_name='\u51fa\u751f\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='testing',
            name='birth_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='testing',
            name='test_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='testing',
            name='test_start',
            field=models.DateField(),
        ),
    ]
