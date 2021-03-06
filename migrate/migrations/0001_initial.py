# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-18 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OldDiscussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=192)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('problem', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OldSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(choices=[('c', 'C'), ('cpp', 'C++'), ('python', 'Python'), ('java', 'Java')], default='cpp', max_length=12)),
                ('code', models.TextField(blank=True)),
                ('problem', models.IntegerField()),
                ('author', models.CharField(max_length=192)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('judge_start_time', models.DateTimeField(blank=True, null=True)),
                ('judge_end_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(-3, 'Waiting'), (-2, 'Judging'), (-1, 'Wrong Answer'), (0, 'Accepted'), (1, 'Time Limit Exceeded'), (2, 'Time Limit Exceeded'), (3, 'Memory Limit Exceeded'), (4, 'Runtime Error'), (5, 'System Error'), (6, 'Compile Error'), (7, 'Idleness Limit Exceeded'), (8, 'Time Limit Exceeded')], default=-3)),
                ('status_percent', models.IntegerField(default=0)),
                ('status_detail', models.TextField(blank=True)),
                ('status_time', models.IntegerField(default=0)),
                ('status_memory', models.IntegerField(default=0)),
                ('code_length', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='OldUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=192)),
                ('password', models.CharField(max_length=192)),
                ('school', models.CharField(max_length=192)),
                ('email', models.CharField(max_length=192)),
            ],
        ),
    ]
