from django.shortcuts import render, get_object_or_404
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
    
def artikel_detail(request, artikel_id):
    artikels = get_object_or_404(Artikel, pk=artikel_id)
    return render(request, 'detail_artikel.html',{
        'artikels' : artikels, 'post_active' : True
    })