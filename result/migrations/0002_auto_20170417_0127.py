# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 19:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='published_date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 4, 16, 19, 57, 30, 23434, tzinfo=utc), null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='result_detail',
            field=models.CharField(default='Result Details...', max_length=50),
        ),
    ]
