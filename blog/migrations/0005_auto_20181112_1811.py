# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181112_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
    ]