from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm


from posts.models import Post
<<<<<<< HEAD
from .models import User, Relationship
=======
from .models import CustomUser, Relationship
from django.contrib.auth.models import User
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86




<<<<<<< HEAD
def view_user(request, user):
    current_user = get_object_or_404(User, username=user)
    posts = Post.objects.all().filter(user=current_user)
=======
def view_user(request, profile):
    current_profile = get_object_or_404(CustomUser, user__username=profile)
    posts = Post.objects.all().filter(profile=current_profile)
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86

    ctx = {"current_user": current_user, "posts": posts}
    return render(request, 'users/view_user.html', ctx)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
<<<<<<< HEAD
=======
            CustomUser.objects.create(user=user)
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86
            return redirect('home')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, "users/register.html", context)

def edit_profile(request):
    form_profile = ProfileUpdateForm()
    if request.method == "POST":
        form_profile = ProfileUpdateForm(request.POST, instance=request.user)
        if form_profile.is_valid():
            user = form_profile.save()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            print("ta jodido")

    context = {'form_profile': form_profile }
    return render(request, "users/edit_profile.html", context)


# Followings
def follow_user(request, user_id):                      
	current_user = request.user            
	to_user = CustomUser.objects.get(id=user_id)   
	rel = Relationship(from_user=current_user, to_user=to_user) 
	rel.save()                                      
	return redirect('home')

def unfollow_user(request, user_id):
	current_user = request.user
	to_user = CustomUser.objects.get(id=user_id)
	rel = Relationship.objects.get(from_user=current_user, to_user=to_user)
	rel.delete()
	return redirect('home')