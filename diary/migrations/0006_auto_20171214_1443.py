# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-14 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_auto_20171214_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]