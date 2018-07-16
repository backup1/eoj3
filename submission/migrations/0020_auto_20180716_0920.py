# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0019_auto_20180713_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.IntegerField(choices=[(-4, 'Submitted'), (-3, 'Waiting'), (-2, 'Judging'), (-1, 'Wrong Answer'), (0, 'Accepted'), (1, 'Time Limit Exceeded'), (2, 'Idleness Limit Exceeded'), (3, 'Memory Limit Exceeded'), (4, 'Runtime Error'), (5, 'System Error'), (6, 'Compile Error'), (7, 'Scored')], db_index=True, default=-4),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status_private',
            field=models.IntegerField(choices=[(-4, 'Submitted'), (-3, 'Waiting'), (-2, 'Judging'), (-1, 'Wrong Answer'), (0, 'Accepted'), (1, 'Time Limit Exceeded'), (2, 'Idleness Limit Exceeded'), (3, 'Memory Limit Exceeded'), (4, 'Runtime Error'), (5, 'System Error'), (6, 'Compile Error'), (7, 'Scored')], default=-4),
        ),
    ]
