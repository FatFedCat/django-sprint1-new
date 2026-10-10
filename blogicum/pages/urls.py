from django.contrib import admin
from django.urls import path

app_name='pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]