# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20170406_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='questions',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
