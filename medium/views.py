from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Artikel
from .forms import Search

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

def detailrespon(request):
    return render(request, 'detail_respon.html')
    
def search(request):
    searchValue =''
    form= Search(request.POST or None)
    if form.is_valid():
        searchValue= form.cleaned_data.get('search')
        
    searchResult= Artikel.objects.filter(judul_artikel__icontains= searchValue)
    context={'form': form,
             'searchResult': searchResult,
             }
    
    return render(request, 'search.html', context)