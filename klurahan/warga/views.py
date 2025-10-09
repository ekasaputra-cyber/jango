from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Warga
# Create your views here.

class WargalistView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga