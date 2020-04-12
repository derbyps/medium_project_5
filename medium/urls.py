from django.urls import path
from . import views

app_name = 'medium'
urlpatterns =[
    path('', views.index, name='index'),
    path('artikel/', views.artikel, name='artikel'),
    path('artikel/<int:artikel_id>/', views.artikel_detail, name='artikel_detail'),
    path('search/', views.search, name='search'),
    path('detailresponse/', views.detailrespon, name='detailrespon')
]