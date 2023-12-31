"""
URL configuration for flightBooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from adminpage import urls as admin_urls
from home import urls as home_urls
from userpage import urls as userpage_urls

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('',include(home_urls)) ,
    path('adminpage/', include(admin_urls, namespace='adminpage')), # ADDED NAMESPACE
    path('userpage/', include(userpage_urls , namespace='userpage')),
   
]
