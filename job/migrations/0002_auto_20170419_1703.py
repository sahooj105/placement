# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliedjob',
            name='student_applied_job_id',
        ),
        migrations.AddField(
            model_name='appliedjob',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]