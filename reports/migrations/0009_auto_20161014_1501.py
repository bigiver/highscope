# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-14 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_remove_type_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sudent_id', models.IntegerField()),
                ('sudent_name', models.CharField(max_length=100)),
                ('birth_Date', models.DateField()),
                ('age', models.IntegerField()),
                ('test_start', models.DateField()),
                ('test_end', models.DateField()),
                ('domain_id', models.IntegerField()),
                ('domain_name', models.CharField(max_length=255)),
                ('types_id', models.IntegerField()),
                ('types_name', models.CharField(max_length=255)),
                ('level_id', models.IntegerField()),
                ('level_name', models.IntegerField()),
                ('level_des', models.CharField(max_length=255)),
                ('testing', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.TextField(verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='level',
            name='num',
            field=models.IntegerField(verbose_name='\u7ea7\u522b'),
        ),
    ]
