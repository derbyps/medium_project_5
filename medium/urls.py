from django.urls import path
from . import views
from .views import SearchResultView

# app_name = 'medium'
urlpatterns =[
    path('', views.index, name='index'),
    path('artikel/', views.artikel, name='artikel'),
    path('artikel/<int:artikel_id>/', views.artikel_detail, name='artikel_detail'),
    path('artikel/clap/<int:artikel_id>/', views.artikel_detail_add_like),
    path('search/', SearchResultView.as_view(), name='search'),
    path('detailresponse/', views.detailrespon, name='detailrespon'),
    path('detailresponse/<int:artikel_id>/', views.respon_detail, name='respon_detail'),
    path('signup/', views.signup, name='signup'),
]