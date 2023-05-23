# blog/urls.py
from django.urls import path
from . import views

app_name = 'hojun'
urlpatterns = [
    path('', views.index, name='index'),
    
]
