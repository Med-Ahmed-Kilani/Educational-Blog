from django.shortcuts import render
from .models import Post, Comment
from .forms import Add_New_Comment, RawPostForm
from rest_framework import viewsets
from .serializers import Postserializer, Commentserializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = Commentserializercomment

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = Postserializer

def post(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def commentView(request, post_id):
    parent = Post.objects.get(pk=post_id)
    cmnt = Comment.objects.filter(post=parent)
    rep = Comment.objects.all()
    nb = len(cmnt)
    return render(request, 'commentView.html', {'cmnt' : cmnt, 'post': parent, 'nb': nb, 'reps': rep})


def repliesView(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    replies = Comment.objects.filter(reply=comment)
    return render(request, 'repliesView.html', {'comnt': comment, 'replies': replies})


def add_post_view(request):
    form = RawPostForm()
    if request.method == 'POST':
        form = RawPostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
    return render(request, 'addPost.html', {'context': form})


def add_comment(request, post_id):
    form = Add_New_Comment()
    post_obj = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = Add_New_Comment(request.POST)
        if form.is_valid():
            Comment.objects.create(comment=form.cleaned_data['comment'], post=post_obj)
    form = Add_New_Comment()
    return render(request, 'addComment.html', {'context': form})


def add_rely(request, comment_id):
    form = Add_New_Comment()
    comment_obj = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        form = Add_New_Comment(request.POST)
        if form.is_valid():
            Comment.objects.create(comment=form.cleaned_data['comment'], reply=comment_obj)
    form = Add_New_Comment
    return render(request, 'addReply.html', {'context': form})

