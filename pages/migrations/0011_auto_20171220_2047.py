# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-20 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20171220_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='images',
            name='max_height',
        ),
        migrations.RemoveField(
            model_name='images',
            name='max_width',
        ),
    ]
