from django.shortcuts import render
from django.http import HttpResponse
from .models import Artikel

# Create your views here.

def index(request):
    return render(request, 'index.html')

def artikel(request):
    artikels = Artikel.objects.all()
    return render(request, 'artikel.html', {
        'artikels' : artikels
    })