# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-07 10:13
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barang', '0007_auto_20191107_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailtransaksi',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='detail_created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detailtransaksi',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 10, 13, 3, 94696)),
        ),
    ]
