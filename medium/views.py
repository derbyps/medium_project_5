from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Artikel, Respon, Users
from .forms import Search
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.

def index(request):
    return render(request, 'index.html')

def artikel(request):
    artikels = Artikel.objects.all()
    paginator = Paginator(artikels, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'artikel.html', {
        # 'artikels' : artikels, 
        'page_obj': page_obj
    })
    
def artikel_detail(request, artikel_id):
    artikels = get_object_or_404(Artikel, pk=artikel_id)
    user = get_object_or_404(Users, pk=5)
    if request.method == 'POST':
        cm = Respon.objects.create(
            artikel = artikels,
            komentator = user,
            komen_artikel = request.POST.get('commenttt'),
            pub_komen = '2020-04-10'
        )
        cm.save()

    return render(request, 'detail_artikel.html',{
        'artikels' : artikels,  
        'post_active' : True
    })

def artikel_detail_add_like(request, artikel_id):
    artikels = get_object_or_404(Artikel, pk=artikel_id)
    cl = artikels.clap
    Artikel.objects.filter(pk=artikel_id).update(clap=cl + 1)
    return redirect('/artikel/'+str(artikel_id)+'/')

def respon_detail(request, artikel_id):
    respons = get_object_or_404(Artikel, pk=artikel_id)
    return render(request, 'detail_respon.html',{
        'repons' : respons, 'post_active' : True
    })

def detailrespon(request):
    respons = Respon.objects.all()
    return render(request, 'detail_respon.html', {
        'respons' : respons
    })
    
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