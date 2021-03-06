# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-05 06:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_unixdatetimefield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barang', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailTransaksi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.IntegerField()),
                ('harga', models.BigIntegerField()),
                ('barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barang.Barang')),
            ],
        ),
        migrations.CreateModel(
            name='TransaksiBarang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=80)),
                ('created_time', django_unixdatetimefield.fields.UnixDateTimeField()),
                ('updated_time', django_unixdatetimefield.fields.UnixDateTimeField()),
                ('jenis_transaksi', models.CharField(choices=[('PENAMBAHAN', 'PENAMBAHAN'), ('PENGURANGAN', 'PENGURANGAN')], max_length=20)),
                ('remark', models.CharField(max_length=100)),
                ('closed', models.BooleanField()),
                ('closed_date', django_unixdatetimefield.fields.UnixDateTimeField()),
                ('closed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='closed_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_created_by', to=settings.AUTH_USER_MODEL)),
                ('detail_barangs', models.ManyToManyField(through='barang.DetailTransaksi', to='barang.Barang')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (),
            },
        ),
        migrations.RemoveField(
            model_name='historybarang',
            name='barang',
        ),
        migrations.RemoveField(
            model_name='historybarang',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historybarang',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='HistoryBarang',
        ),
        migrations.AddField(
            model_name='detailtransaksi',
            name='transaksi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='barang.TransaksiBarang'),
        ),
    ]
