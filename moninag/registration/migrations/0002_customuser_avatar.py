# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-24 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.CharField(
                default=b'', editable=False, max_length=1000),
        ),
    ]
