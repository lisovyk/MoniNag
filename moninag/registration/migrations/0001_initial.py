# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(
                    max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=254)),
                ('second_name', models.CharField(blank=True, max_length=254)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
