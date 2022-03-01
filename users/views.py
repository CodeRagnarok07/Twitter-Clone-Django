from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def register(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')

def view_user(request):
    return render(request, 'users/view_user.html')