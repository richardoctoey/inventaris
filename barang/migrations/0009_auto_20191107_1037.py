# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-07 10:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0008_auto_20191107_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaksibarang',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='transaksibarang',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='transaksibarang',
            name='updated_time',
        ),
        migrations.AddField(
            model_name='barang',
            name='created_by',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='barang',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 10, 36, 48, 81772)),
        ),
        migrations.AddField(
            model_name='barang',
            name='modified_by',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='barang',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 10, 36, 48, 81801)),
        ),
        migrations.AddField(
            model_name='transaksibarang',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 10, 36, 48, 82166)),
        ),
        migrations.AddField(
            model_name='transaksibarang',
            name='modified_by',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaksibarang',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 10, 36, 48, 82194)),
        ),
        migrations.AlterField(
            model_name='detailtransaksi',
            name='created_by',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='detailtransaksi',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 7, 10, 36, 48, 82828)),
        ),
        migrations.AlterField(
            model_name='transaksibarang',
            name='closed_by',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='transaksibarang',
            name='created_by',
            field=models.CharField(max_length=50),
        ),
    ]
