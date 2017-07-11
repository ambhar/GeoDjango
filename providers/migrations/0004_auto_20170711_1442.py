# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0003_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='polygon',
            field=geoposition.fields.GeopositionField(max_length=42),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
