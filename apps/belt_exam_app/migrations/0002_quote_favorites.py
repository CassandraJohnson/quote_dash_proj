# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-18 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='favorites',
            field=models.ManyToManyField(related_name='movies_favorited', to='belt_exam_app.User'),
        ),
    ]
