from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

# def register(request):
#     return render(request, 'home.html')

# def login(request):
#     return render(request, 'home.html')

# def user_view(request):
#     return render(request, 'home.html')