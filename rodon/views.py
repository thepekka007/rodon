from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from django.db import models
from django.contrib.auth.models import User, auth
from . models import *
# Create your views here.


def rodon_index(request):
    return render(request,'rodon_index.html')


def home(request):
    return render(request,'rodon_index.html')

def about(request):
    return render(request,'rodon_about.html')


def contact(request):
    return render(request,'rodon_contact.html')


def login(request):

    data = Contactdata.objects.all().order_by('-id')
    return render(request,'login.html',{'data':data})



def logindata(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        # Authenticate user
        user = auth.authenticate(username=username, password=password)
    
        if user is not None:
            # If user is authenticated, log them in
            auth.login(request, user)
            # Fetch and render admin page with required data
            data = Contactdata.objects.all().order_by('-id')
            return render(request, 'admin.html', {'data': data})
        else:
            # If user authentication fails, return to login page with error message
            error_message = "Invalid email or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        # If request method is not POST (e.g., GET), render the login page
        return render(request, 'login.html')

def sendmessage(request):

    if request.method == 'POST':
            debit = Contactdata(
                name = request.POST['name'],
                email = request.POST['email'],
                subject = request.POST['subject'],
                message = request.POST['message'],
                phone = request.POST['phone'],
                
                )

            debit.save()
            return render(request,'rodon_contact.html')
