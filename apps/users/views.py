from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm


from posts.models import Post
from .models import User, Relationship




def view_user(request, user):
    current_user = get_object_or_404(User, username=user)
    posts = Post.objects.all().filter(user=current_user)

    ctx = {"current_user": current_user, "posts": posts}
    return render(request, 'users/view_user.html', ctx)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
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