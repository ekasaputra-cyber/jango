from django.urls import path
from .views import WargalistView, WargaDetailView, PengaduanListView

urlpatterns = [
    path('', WargalistView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='wargadetail-list'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
]