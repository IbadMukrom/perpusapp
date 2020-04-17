from django.db import models

# Create your models here.

class Anggota(models.Model):
    nama = models.CharField(max_length=100, blank=False, null=False)
    alamat = models.CharField(max_length=100, blank=False, null=False)
    pekerjaan = models.CharField(max_length=100, blank=True, null=True)
    umur = models.PositiveIntegerField()
    no_hp = models.CharField( unique=True, max_length=12)

    def __str__(self):
        return self.nama

class Buku(models.Model):
    KATEGORI_BUKU = (
        ('sains', 'sains' ),
        ('sosial', 'sosial'),
        ('fiksi', 'fiksi'),
        ('astronomi','astronomi'),
        ('humor', 'humor'),
    )

    nama_buku = models.CharField(max_length=100, blank=False, null=False)
    nama_pengarang = models.CharField(max_length=100, blank=True, null=True)
    kategori = models.CharField(max_length=100, choices=KATEGORI_BUKU)
    jumlah_buku = models.PositiveIntegerField()

    def __str__(self):
        return self.nama_buku

class Transaksi_Peminjaman(models.Model,):
    STATUS =(
        ('masih dipinjam', 'masih dipinjam'),
        ('sudah dikembalikan', 'sudah dikembalikan'),
    )

    peminjam = models.ForeignKey(Anggota, on_delete=models.CASCADE)
    judul_buku = models.ForeignKey(Buku, on_delete=models.CASCADE)
    status_buku = models.CharField(choices=STATUS, null=False, max_length=50)
    tgl_pinjam = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    class Meta:
        unique_together =('peminjam','judul_buku')

    def __str__(self):
        return self.status_buku
    
    