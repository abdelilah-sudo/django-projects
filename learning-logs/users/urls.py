"""Defines URL patterns for users"""
from django.urls import path, include
from .views import *
app_name = 'users'
urlpatterns = [
 # Include default auth urls.
path('', include('django.contrib.auth.urls')),
path('register/', register, name='register'),
]