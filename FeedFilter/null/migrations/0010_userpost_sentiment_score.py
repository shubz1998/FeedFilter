# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-04 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('null', '0009_auto_20180304_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='sentiment_score',
            field=models.FloatField(default=0.0),
        ),
    ]
