from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import Add_New_Comment, RawPostForm, register_form
from rest_framework import viewsets
from .serializers import Postserializer, Commentserializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Commentserializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer


def post(request):
    posts = Post.objects.order_by('-createdAt')
    return render(request, 'index.html', {'posts': posts})


def commentView(request, post_id):
    parent = Post.objects.get(pk=post_id)
    cmnt = Comment.objects.filter(post=parent)
    rep = Comment.objects.all()
    nb = len(cmnt)
    return render(request, 'commentView.html', {'cmnt': cmnt, 'post': parent, 'nb': nb, 'reps': rep})


def repliesView(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    replies = Comment.objects.filter(reply=comment)
    return render(request, 'repliesView.html', {'comnt': comment, 'replies': replies})


@login_required
def add_post_view(request):
    request.user
    form = RawPostForm()
    if request.method == 'POST':
        form = RawPostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            Post.objects.create(post=form.cleaned_data['post'], upload=form.cleaned_data['upload'], user=request.user)
            return redirect("/")
    return render(request, 'addPost.html', {'context': form})


@login_required
def add_comment(request, post_id):
    post_obj = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = Add_New_Comment(request.POST)
        if form.is_valid():
            Comment.objects.create(comment=form.cleaned_data['comment'], post=post_obj)
    form = Add_New_Comment()
    return render(request, 'addComment.html', {'context': form})


@login_required
def add_rely(request, comment_id):
    form = Add_New_Comment()
    comment_obj = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        form = Add_New_Comment(request.POST)
        if form.is_valid():
            Comment.objects.create(comment=form.cleaned_data['comment'], reply=comment_obj)
    form = Add_New_Comment
    return render(request, 'addReply.html', {'context': form})


def register(request):
    if request.method == 'POST':
        form = register_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are able now to log in ')
            return redirect("/Login")
    else:
        form = register_form()
    return render(request, 'Users/Register.html', {'form': form})


@login_required
def profile(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'Users/Profile.html', {'posts': posts})