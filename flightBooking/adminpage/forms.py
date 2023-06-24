from django import forms
from .models import Flight

from django.urls import path
from . import views

urlpatterns = [
    path('admin_home/', views.admin_home, name='admin_home'),
    path('add_flight/', views.add_flight, name='add_flight'),
    path('remove_flight/', views.remove_flight, name='remove_flight'),
]
