from django.shortcuts import render,redirect
from .models import *
from .forms import *
from users.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

@login_required
def index(request):
    comment_form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            post_id=request.POST.get('post_id')
            post=get_object_or_404(Post, id=post_id)
            new_comment.post=post
            new_comment.user=request.user
            new_comment.save()
    current_user=request.user
    posts=Post.objects.filter(user=current_user)
    profile=Profile.objects.filter(user=current_user).first()
    return render(request, 'index.html',{
        'posts':posts,
        'profile':profile,
        'comment_form':comment_form,
    })   


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.user=request.user
            item.save()
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form':form})


@login_required
def feed(request):
    comment_form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            post_id=request.POST.get('post_id')
            post=get_object_or_404(Post, id=post_id)
            new_comment.post=post
            new_comment.user=request.user
            new_comment.save()
    posts=Post.objects.all()
    return render(request, 'feed.html',{
        'posts':posts,
        'user':request.user,
        'comment_form':comment_form,
    })

def liked_by(request):
    post_id=request.POST.get('post_id')
    post=get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    return redirect('feed')