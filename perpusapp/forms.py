from perpusapp.models import Buku, Anggota, Transaksi_Peminjaman
from django.forms import ModelForm
from perpusapp.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AnggotaForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = '__all__'

class BukuForm(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

class Transaksi_PeminjamanForm(forms.ModelForm):
    class Meta:
        model = Transaksi_Peminjaman
        fields = ['peminjam','judul_buku','status_buku']  

class Signupform(UserCreationForm):
    nama_depan = forms.CharField(max_length=20)
    nama_belakang = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)

    class Meta:
        models = User
        fields = ('username', 'nama_belakang', 'nama_belakang', 'email','password1', 'password2')

