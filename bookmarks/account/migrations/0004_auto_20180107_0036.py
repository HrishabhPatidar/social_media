# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-06 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180107_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='user/%y/%m/%d'),
        ),
    ]