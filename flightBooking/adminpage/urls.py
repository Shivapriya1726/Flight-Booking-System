from django.urls import path
from . import views

app_name = 'adminpage'

urlpatterns = [
    path('login/' , views.login,name='login'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('add_flight/', views.add_flight, name='add_flight'),
    path('remove_flight/', views.remove_flight, name='remove_flight'),
    
]