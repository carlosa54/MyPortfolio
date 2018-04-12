# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-31 17:40
from __future__ import unicode_literals

import apps.projects.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_work_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.projects.models.logo_upload_to),
        ),
    ]
