# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-15 18:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_logins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_address',
            field=models.CharField(max_length=255, unique=True, validators=[django.core.validators.EmailValidator('Invalid email')]),
        ),
    ]