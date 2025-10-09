from django.urls import path
from .views import WargalistView, WargaDetailView

urlpatterns = [
    path('', WargalistView.as_view(), name='warga-list'),
    path('<int:pk>', WargaDetailView.as_view(), name='wargadetail-list'),
]