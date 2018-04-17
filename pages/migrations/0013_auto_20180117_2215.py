# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-17 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20180115_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(max_length=80)),
                ('skype', models.CharField(blank=True, max_length=80)),
                ('mob_phone', models.CharField(blank=True, max_length=80)),
                ('rob_phone', models.CharField(blank=True, max_length=80)),
                ('facebook_link', models.CharField(blank=True, max_length=80)),
                ('twitter_link', models.CharField(blank=True, max_length=80)),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.DeleteModel(
            name='Footer',
        ),
    ]