from django.shortcuts import render
from post.forms import AddPostForm
from post.models import Post
from django.shortcuts import render, redirect


def post(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'post.html', {
        'posts': posts
    })


def create_post(request):

    form = AddPostForm()

    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')

    return render(request, 'add-post.html', {
        'form': form
    })


def get_post(request):
    post = Post.objects.get(id=1)
    return render(request, 'get-post.html', {
        post: post
    })


def edit_post(request, id):
    post = Post.objects.get(id=id)
    form = AddPostForm(instance=post)
    if request.method == 'POST':
        form = AddPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post')
    return render(request, 'edit-post.html', {
        'form': form
    })


def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('post')
