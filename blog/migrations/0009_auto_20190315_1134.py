# Generated by Django 2.1.7 on 2019-03-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190112_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='edit_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='hide_revisions',
            field=models.BooleanField(default=False, verbose_name='历史版本仅自己可见'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=128, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='visible',
            field=models.BooleanField(default=True, verbose_name='对所有用户可见'),
        ),
    ]
