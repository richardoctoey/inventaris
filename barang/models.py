# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_unixdatetimefield import UnixDateTimeField
from django.conf import settings
from django.db.models import Sum
from datetime import datetime

class Simple(models.Model):
    name = models.CharField(max_length=10)

class Barang(models.Model):
    kode = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=50)
    harga = models.BigIntegerField()
    created_by = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=datetime.now())
    modified_by = models.CharField(max_length=50)
    modified_date = models.DateTimeField(default=datetime.now())

    stok = 0

    def add_barang(self, kb, nb, hb, sab):
        b = self.objects.create(kode=kb, nama=nb, harga=hb)
        DetailTransaksi.objects.create(barang=b, action_from=0, harga=hb, jumlah=sab)

    def stokAkhir(self):
        subqs = DetailTransaksi.objects.filter(barang=self)
        stok = subqs.aggregate(Sum('jumlah'))['jumlah__sum']
        return stok

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        isaved = False
        s = None
        try:
            s = super(Barang, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
            isaved = True
        except:
            isaved = False
        if isaved == True:
            DetailTransaksi.objects.create(barang=self, action_from=0, harga=self.harga, jumlah=self.stok, created_by=self.created_by)
        return s


    def __str__(self):
        return self.nama



class TransaksiBarang(models.Model):
    invoice_no = models.CharField(max_length=80)
    detail_barangs = models.ManyToManyField('Barang', through='DetailTransaksi')
    remark = models.CharField(max_length=100)
    created_by = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=datetime.now())
    modified_by = models.CharField(max_length=50)
    modified_date = models.DateTimeField(default=datetime.now())
    closed = models.BooleanField()
    closed_date = UnixDateTimeField()
    closed_by = models.CharField(max_length=50)

    # class Meta:
    #     permissions = [
    #         ("add", "Tambah Transaksi"),
    #         ("hapus", "Hapus Transaksi"),
    #         ("edit", "Edit Transaksi"),
    #         ("close", "Closing Transaksi"),
    #     ]

class DetailTransaksi(models.Model):
    ACTIONCHOICE = (
        (0, "INIT"),
        (1, "PENYESUAIAN"),
        (2, "TRANSAKSI_SALES"),
    )
    transaksi = models.ForeignKey(TransaksiBarang, null=True, blank=True)
    barang = models.ForeignKey(Barang)
    jumlah = models.IntegerField()
    harga = models.BigIntegerField()
    action_from = models.SmallIntegerField(choices=ACTIONCHOICE)
    created_by = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=datetime.now())
