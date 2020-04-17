from django.shortcuts import render, redirect
from perpusapp.models import Anggota, Buku, Transaksi_Peminjaman
from perpusapp.forms import AnggotaForm, BukuForm, Transaksi_PeminjamanForm,Signupform
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@login_required
def home(request):
    total_buku = Buku.objects.aggregate(Sum('jumlah_buku')) ['jumlah_buku__sum']
    total_anggota = Anggota.objects.count()    
    peminjaman = Transaksi_Peminjaman.objects.all()
    total_peminjaman = peminjaman.count()
    
    dipinjam = Transaksi_Peminjaman.objects.filter(status_buku='masih dipinjam').count()
    dikembalikan = Transaksi_Peminjaman.objects.filter(status_buku='sudah dikembalikan').count()

    data = {'total_peminjaman': total_peminjaman, 'total_buku': total_buku,
    "total_anggota": total_anggota, "dipinjam": dipinjam,
    "dikembalikan": dikembalikan}
    return render (request, 'perpus/dashboard.html',data)

@login_required
def peminjaman(request):
    peminjaman = Transaksi_Peminjaman.objects.all()
    data = {'peminjaman': peminjaman}
    return render (request, 'perpus/peminjaman.html', data )

@login_required
def tambah_peminjaman(request):
    form = Transaksi_PeminjamanForm()
    if request.method=='POST':
        form = Transaksi_PeminjamanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/peminjaman/')
                      
        elif not form.is_valid():       
            messages.warning(request,"data tersebut sudah ada")
            data = {'form':form}
            return render (request, 'perpus/form_peminjaman.html', data)
    
    else:
        data = {'form':form}
        return render (request, 'perpus/form_peminjaman.html', data)

@login_required
def edit_peminjaman(request, id):
    peminjam = Transaksi_Peminjaman.objects.get(id=id)
    form = Transaksi_PeminjamanForm(instance=peminjam)
    if request.method=='POST':
        form = Transaksi_PeminjamanForm(request.POST, instance=peminjam)
        if not form.is_valid():
            messages.warning(request,"data tersebut sudah ada")
            data = {'form':form}
            return render (request, 'perpus/form_peminjaman.html',data )  
        
        if form.is_valid():
            form.save()
            return redirect('/peminjaman/')
    context={'form':form}
    return render(request, 'perpus/form_peminjaman.html', context)

@login_required
def hapus_peminjaman(request, id):
    peminjam = Transaksi_Peminjaman.objects.get(id=id)
    peminjam.delete()
    return redirect('/peminjaman/')

@login_required
def data_buku (request):
    buku = Buku.objects.all()
    return render(request, 'perpus/buku.html', {'buku':buku})

@login_required
def tambah_buku(request):
    form = BukuForm()
    if request.method=='POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/buku/')
    context = {'form': form}
    return render (request, 'perpus/buku_form.html', context)

@login_required
def hapus_buku(r, id):
    buku = Buku.objects.get(id=id)
    buku.delete()
    return redirect ('/buku')

@login_required
def edit_buku(request, id):
    buku = Buku.objects.get(id=id)
    form = BukuForm(instance=buku)

    if request.method=="POST":
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            return redirect('/buku/')
    context = {'form': form}
    return render (request, 'perpus/buku_form.html', context)

@login_required
def data_anggota(request):
    anggotas = Anggota.objects.all()
    return render (request, 'perpus/anggota.html', {'anggotaaa':anggotas})

@login_required
def tambah_anggota(request):
    form = AnggotaForm()
    if request.method=='POST':
        form = AnggotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/anggota/')
    data = {'form': form}
    return render (request, 'perpus/anggota_form.html', data)

@login_required
def edit_anggota(r, id):
    anggota = Anggota.objects.get(id=id)
    form = AnggotaForm(instance=anggota)

    if r.method=="POST":
        form = AnggotaForm(r.POST, instance=anggota)
        if form.is_valid():
            form.save()
            return redirect('/anggota/')
    else:
        return render (r, 'perpus/anggota_form.html', {'form':form})

@login_required
def hapus_anggota(request,id):
    anggotas = Anggota.objects.get(id=id)
    anggotas.delete()
    return redirect('/anggota/')

def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = raw_password)
            login = (request, user)
            return redirect('/accounts/login/')
        elif not form.is_valid():
            form = UserCreationForm()
            messages.warning(request,"pastikan username & password anda sudah benar")
            return render (request, 'registration/signup.html', {'form':form})    
    else:
        form = UserCreationForm()
        return render (request, 'registration/signup.html', {'form':form})