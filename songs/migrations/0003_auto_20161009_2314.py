# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 23:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20161009_1806'),
        ('songs', '0002_artist_artistimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.CharField(max_length=150),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.AddField(
            model_name='songrate',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Song'),
        ),
        migrations.AddField(
            model_name='songrate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User'),
        ),
    ]