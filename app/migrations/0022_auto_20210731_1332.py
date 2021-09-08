# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-31 10:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20210731_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 7, 31, 13, 32, 47, 379347), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 7, 31, 13, 32, 47, 380347), verbose_name='Дата'),
        ),
    ]
