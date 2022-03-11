from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

from django.contrib import messages

from .models import Profile, Post
from .forms import UserRegisterForm

@login_required
def home(request):
    posts = Post.objects.all()
    ctx = {"posts": posts}
    return render(request, 'users/home.html', ctx)


@login_required
def view_user(request):
    return render(request, 'users/view_user.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(user=user)
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, "users/register.html", context)
