# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_info', models.CharField(default='', max_length=50, verbose_name='\u6807\u9898')),
                ('img', models.ImageField(upload_to='banner/', verbose_name='\u8f6e\u64ad\u56fe')),
                ('link_url', models.URLField(max_length=100, verbose_name='\u56fe\u7247\u94fe\u63a5')),
                ('is_active', models.BooleanField(default=False, verbose_name='\u662f\u5426\u662factive')),
            ],
            options={
                'verbose_name': '\u8f6e\u64ad\u56fe',
                'verbose_name_plural': '\u8f6e\u64ad\u56fe',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u94fe\u63a5\u540d\u79f0')),
                ('linkurl', models.URLField(max_length=100, verbose_name='\u7f51\u5740')),
            ],
            options={
                'verbose_name': '\u53cb\u60c5\u94fe\u63a5',
                'verbose_name_plural': '\u53cb\u60c5\u94fe\u63a5',
            },
        ),
        migrations.CreateModel(
            name='Tui',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u63a8\u8350\u4f4d')),
            ],
            options={
                'verbose_name': '\u63a8\u8350\u4f4d',
                'verbose_name_plural': '\u63a8\u8350\u4f4d',
            },
        ),
    ]