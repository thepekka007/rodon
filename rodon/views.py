from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
# Create your views here.


def rodon_index(request):
    return render(request,'rodon_index.html')


def home(request):
    return render(request,'rodon_index.html')

def about(request):
    return render(request,'rodon_about.html')


def contact(request):
    return render(request,'rodon_contact.html')
def admin(request):
    return render(request,'admin.html')
