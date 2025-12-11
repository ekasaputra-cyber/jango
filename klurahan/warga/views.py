# warga/views.py

from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from .models import Warga, Pengaduan
from .forms import WargaForm, PengaduanForm

# --- Django REST Framework Imports ---
from rest_framework import viewsets
# from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import WargaSerializer, PengaduanSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter 

# =====================================================
# Regular Django Views (for web templates)
# =====================================================

class WargalistView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'daftar_warga'
    ordering = ['nama']


class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    context_object_name = 'warga'


class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')


class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')


class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')


class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'daftar_pengaduan'
    ordering = ['-tanggal_pengaduan']


class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')


class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    success_url = reverse_lazy('pengaduan-list')


class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'
    success_url = reverse_lazy('pengaduan-list')

# =====================================================
# Django REST Framework API Views (for JSON endpoints)
# =====================================================

# class WargaListAPIView(ListAPIView):
#     """API endpoint for listing all Warga"""
#     queryset = Warga.objects.all()
#     serializer_class = WargaSerializer


# class WargaDetailAPIView(RetrieveAPIView):
#     """API endpoint for retrieving a single Warga by ID"""
#     queryset = Warga.objects.all()
#     serializer_class = WargaSerializer


# class PengaduanListAPIView(ListAPIView):
#     """API endpoint for listing all Pengaduan"""
#     queryset = Pengaduan.objects.all()
#     serializer_class = PengaduanSerializer


# class PengaduanDetailAPIView(RetrieveAPIView):
#     """API endpoint for retrieving a single Pengaduan by ID"""
#     queryset = Pengaduan.objects.all()
#     serializer_class = PengaduanSerializer

class WargaViewSet(viewsets.ModelViewSet):
    """API endpoint for listing all Warga"""
    queryset = Warga.objects.all().order_by('-tanggal_registrasi')
    serializer_class = WargaSerializer
    permissions_classes=[IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nama_lengkap', 'nik', 'alamat']
    ordering_fields = ['nama_lengkap', 'tanggal_registrasi']


class PengaduanViewSet(viewsets.ModelViewSet):
    """API endpoint for listing all Pengaduan"""
    queryset = Pengaduan.objects.all().order_by('-tanggal_pengaduan')
    serializer_class = PengaduanSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['judul', 'isi']
    ordering_fields = ['judul', 'tanggal_pengaduan','status']