from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
import requests

from djangoTamimStore.forms import PostForm
from .models import Post


def product_list(request):
    response = requests.get('https://fakestoreapi.com/products')
    products = response.json()
    return render(request, 'store/product_list.html', {'products': products})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form': form})


def product_detail(request, pk):
    response = requests.get(f'https://fakestoreapi.com/products/{pk}')
    product = response.json()
    if response.status_code == 200:
        return render(request, 'store/product_detail.html', {'product': product})
    else:
        return render(request, 'store/404.html')


def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'registration/user_detail.html', {'user': user})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.user:
        return redirect('post_detail', pk=post.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.user:
        return redirect('post_detail', pk=post.pk)
    post.delete()
    return redirect('post_list')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def about(request):
    return render(request, 'about.html')
