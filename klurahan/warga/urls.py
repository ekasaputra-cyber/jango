from django.urls import path
from .views import WargalistView, WargaDetailView, PengaduanListView, WargaCreateView, PengaduanCreateView, WargaUpdateView, WargaDeleteView, PengaduanUpdateView, PengaduanDeleteView

urlpatterns = [
    path('', WargalistView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'), # URL untuk form tambah
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'), # URL untuk edit warga
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'), # URL untuk hapus warga
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'), # URL untuk form pengaduan baru
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'), # URL edit pengaduan
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'), # URL hapus pengaduan
]