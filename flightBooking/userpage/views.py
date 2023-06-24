from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

def signup(request):
    return render(request,'signup.html')
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'user@gmail.com' and password == 'user123':
            # Authentication successful
            return render(request ,'user_home.html')
    

    return render(request,'loginuser.html' )