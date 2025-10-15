from django.urls import path
from .views import WargalistView, WargaDetailView, PengaduanListView, WargaCreateView, PengaduanCreateView

urlpatterns = [
    path('', WargalistView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'), # URL untuk form tambah
    path('<int:pk>/', WargaDetailView.as_view(), name='wargadetail-list'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'), # URL untuk form pengaduan baru
]