# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 14:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0004_auto_20170711_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
    ]
