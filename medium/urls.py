from django.urls import path
from . import views

app_name = 'medium'
urlpatterns =[
    path('', views.index, name='index'),
]