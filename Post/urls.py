from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as post_views

urlpatterns = [
    path('', post_views.post, name='Home'),
    path('commentView/<int:post_id>/', post_views.commentView, name='commentView'),
    path('addComment/<int:post_id>/', post_views.add_comment, name='addComment'),
    path('addReply/<int:comment_id>/', post_views.add_rely, name='addReply'),
    path('repliesView/<int:comment_id>/', post_views.repliesView, name='repliesView'),
    path('addPost/', post_views.add_post_view, name='addpost'),
    path('Register/', post_views.register, name='register'),
    path('Login/', auth_views.LoginView.as_view(template_name='Users/Login.html'), name='login'),
    path('Logout/', auth_views.LogoutView.as_view(template_name='Users/Logout.html'), name='logout'),
    path('Profile/', post_views.profile, name='profile'),
]
