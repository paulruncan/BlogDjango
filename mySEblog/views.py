from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import title
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mySEblog.models import Post
from mySEblog.forms import PostForm, EditForm
from django.urls import reverse_lazy
from reviews.forms import ReviewForm
from django.contrib import messages

from reviews.models import Review


# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    return render(request, 'homepage.html', {'posts': posts})

def postview(request, pk):
    post = Post.objects.get(id=pk)
    reviews = Review.objects.filter(post=post)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.post = post
            review.created_by = request.user
            review.save()
            return redirect('postview', pk=pk)
    else:
        review_form = ReviewForm()
    context = {
        'post': post,
        'reviews': reviews,
        'review_form': review_form
        }
    return render(request, 'postview.html', context)
@login_required
def addpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('homepage')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'add_post.html', context)
@login_required
def editpost(request, pk):
    post = get_object_or_404(Post, pk=pk)

    form = EditForm(instance=post)
    if post.author != request.user and not request.user.is_superuser:
        messages.error(request, "You are not allowed to edit this post.")
        return redirect('postview', pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PostForm(instance=post)

    context = {'form': form}
    return render(request, 'update_post.html', context)

def search_posts(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(title__icontains=query)
    return render(request, 'search_posts.html', {'posts': posts, 'query': query})


@login_required
def deletepost(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Restrict access to the post author
    if post.author != request.user and not request.user.is_superuser:
        messages.error(request, "You are not allowed to delete this post.")
        return redirect('postview', pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Your post has been successfully deleted.")
        return redirect('homepage')

    context = {'post': post}
    return render(request, 'delete_post.html', context)