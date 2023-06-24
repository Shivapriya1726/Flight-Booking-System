from django.urls import path
from userpage import views

app_name = 'userpage'

urlpatterns = [
    path('signup/' , views.signup, name='signup'),
    path('loginuser/' , views.loginuser, name='loginuser'),
    
]                                 