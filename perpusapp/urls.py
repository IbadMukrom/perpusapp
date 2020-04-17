from django.urls import path
from . import views
urlpatterns = [
    path ('', views.home, name='home'),

    path ('peminjaman/', views.peminjaman, name='peminjaman'),
    path ('tambah_peminjaman/', views.tambah_peminjaman, name='tambah_peminjam'),
    path ('edit_peminjaman/<int:id>/', views.edit_peminjaman, name='edit_peminjaman'),
    path ('hapus_peminjaman/<int:id>/', views.hapus_peminjaman, name='hapus_peminjaman'),

    path ('buku/', views.data_buku, name='data_buku'),
    path ('tambah_buku/',views.tambah_buku, name='tambah_buku'),
    path ('edit_buku/<int:id>',views.edit_buku, name='edit_buku'),
    path ('hapus_buku/<int:id>',views.hapus_buku, name='hapus_buku'),

    path ('anggota/', views.data_anggota,name='data_anggota'),
    path ('tambah_anggota/', views.tambah_anggota,name='tambah_anggota'),
    path ('hapus_anggota/<int:id>/',views.hapus_anggota, name='hapus_anggota'),
    path ('edit_anggota/<int:id>/',views.edit_anggota, name='edit_anggota'),

    path ('signup/', views.signup, name='signup'),



]