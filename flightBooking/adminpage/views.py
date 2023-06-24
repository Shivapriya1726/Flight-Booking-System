from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate

def login(request):
    if request.method == 'POST':
        
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == 'admin' and password == 'admin123':
            # Authentication successful
            return render(request ,'admin_home.html')
    
    
    return render(request, 'login.html')

from django.shortcuts import render, redirect
from .models import Flight

def admin_home(request):
    flights = Flight.objects.all()
    context = {
        'flights': flights
    }
    return render(request, 'admin_home.html', context)

def add_flight(request):
    if request.method == 'POST':
        # Extract the form data and create a new flight object
        # Save the flight object to the database
        # Redirect to the admin home page or any other desired page
        return redirect('admin_home')
    else:
        return render(request, 'admin_home.html')

def remove_flight(request):
    if request.method == 'POST':
        flight_id = request.POST['flight_id']
        # Remove the flight with the given ID from the database
        # Redirect to the admin home page or any other desired page
        return redirect('admin_home')
