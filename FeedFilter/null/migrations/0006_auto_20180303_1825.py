# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('null', '0005_blockedpost_stats_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stats',
            old_name='count_0',
            new_name='count',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='count_1',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='count_2',
        ),
        migrations.RemoveField(
            model_name='stats',
            name='count_3',
        ),
        migrations.AlterField(
            model_name='blockedpost',
            name='post_type',
            field=models.CharField(choices=[(b'0', b'image'), (b'1', b'text')], max_length=1, null=True),
        ),
    ]
