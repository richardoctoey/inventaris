# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from barang.models import *
from django.contrib import admin
from django.db.models import Sum
from django import forms

# Register your models here.

class FormTambah(forms.ModelForm):
    stok = forms.IntegerField()
    class Meta:
        fields = (
            'kode', 'nama', 'harga', 'stok',
        )
        model = Barang

    def clean(self):
        cleaned_data = super(FormTambah, self).clean()
        self.stok = cleaned_data.get("stok")
        self.Meta.model.stok = cleaned_data.get("stok")
        return cleaned_data


class BarangAdmin(admin.ModelAdmin):
    list_display = ('kode', 'nama', 'harga', 'stok')

    def stok(self, obj):
        return obj.stokAkhir()

    def get_form(self, request, obj=None, **kwargs):
        if obj == None:
            self.form = FormTambah
        return super(BarangAdmin, self).get_form(request=request, obj=obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if obj.pk == None:
            obj.created_by = request.user
            obj.created_date = datetime.now()
        else:
            obj.modified_by = request.user
            obj.modified_date = datetime.now()

        super(BarangAdmin, self).save_model(request, obj, form, change)

class DetailTransaksiAdmin(admin.ModelAdmin):
    list_display = ('transaksi', 'barang', 'jumlah', 'action_from')


class TransaksiAdmin(admin.ModelAdmin):
    pass

admin.site.register(Barang, BarangAdmin)
admin.site.register(TransaksiBarang, TransaksiAdmin)
admin.site.register(DetailTransaksi, DetailTransaksiAdmin)

