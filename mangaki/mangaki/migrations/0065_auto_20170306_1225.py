# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 12:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0064_trope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coldstartrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cold_start_rating', to=settings.AUTH_USER_MODEL),
        ),
    ]
