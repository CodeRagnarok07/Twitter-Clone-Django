from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile, Relationship
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from posts.models import Post




def view_user(request, profile):
    current_profile = get_object_or_404(Profile, user__username=profile)
    posts = Post.objects.all().filter(profile=current_profile)

    ctx = {"current_profile": current_profile, "posts": posts}
    return render(request, 'users/view_user.html', ctx)


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

def edit_profile(request):
    form_user = UserUpdateForm()
    form_profile = ProfileUpdateForm()
    if request.method == "POST":
            form_user = UserUpdateForm(request.POST, instance=request.user)
            form_profile = ProfileUpdateForm(request.POST, instance=request.user.profile)
            if form_user.is_valid() and form_profile.is_valid():
                user = form_user.save()
                profile = form_profile.save(commit=False)
                profile.user = user
                profile.save()
                login(request, user)
                return redirect("home")

    context = {'form_user': form_user, 'form_profile': form_profile }
    return render(request, "users/edit_profile.html", context)


# Followings
def follow_user(request, user_id):                      
	current_user = request.user            
	to_user = User.objects.get(id=user_id)   
	rel = Relationship(from_user=current_user, to_user=to_user) 
	rel.save()                                      
	return redirect('home')

def unfollow_user(request, user_id):
	current_user = request.user
	to_user = User.objects.get(id=user_id)
	rel = Relationship.objects.get(from_user=current_user, to_user=to_user)
	rel.delete()
	return redirect('home')