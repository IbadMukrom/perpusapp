from django.contrib import admin
from perpusapp.models import Anggota, Buku, Transaksi_Peminjaman
# Register your models here.
admin.site.register(Anggota)
admin.site.register(Buku)
admin.site.register(Transaksi_Peminjaman)
