# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='anonymous_user.jpg', upload_to=b''),
        ),
    ]
