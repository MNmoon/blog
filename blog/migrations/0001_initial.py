# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u6587\u7ae0\u6807\u7b7e')),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u6807\u7b7e',
                'verbose_name_plural': '\u6587\u7ae0\u6807\u7b7e',
            },
        ),
    ]