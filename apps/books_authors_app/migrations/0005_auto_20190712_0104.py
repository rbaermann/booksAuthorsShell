# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-12 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0004_auto_20190711_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]