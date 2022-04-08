from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all()
    # New twit
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # aqui si se necesita agregar que usuario hace el post
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm
    ctx = {"posts": posts, "form":form}

    return render(request, 'posts/home.html', ctx)