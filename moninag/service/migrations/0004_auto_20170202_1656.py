# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_service_server'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('', 'Unknown'), ('fail', 'Fail'), ('ok', 'OK')], default='', max_length=10),
        ),
    ]
