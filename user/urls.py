from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
