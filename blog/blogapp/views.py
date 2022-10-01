# from django.http import request
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import *
from .models import Post
from django.views.generic.edit import CreateView

posts = Post.objects.all()


def HomePageView(request):
    posts = Post.objects.all()
    # dict = request.POST
    # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    # user.save
    # Post.objects.create(
    #     title = dict['title'],
    #     author = user,
    #     body = dict['body'],
    #     slug = dict['slug']
    # )
    # print(posts)
    return render(request, 'blog/home.html', {'posts': posts})


def PostDetailView(request, slug):
    post = posts.get(slug=slug)
    return render(request, 'blog/post_data.html', {'post': post})


def PostCreateView(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
            # try:
            #     # Post.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(None, 'Ошибка добавления поста')

    else:
        form = AddPostForm()
    return render(request, 'blog/post_new.html', {'form':form})



# Create your views here.
