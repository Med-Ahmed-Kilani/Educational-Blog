from django.urls import path
from . import views

urlpatterns = [
    path('', views.post, name='index'),
    path('<int:post_id>/commentView/', views.commentView, name='commentView'),
    path('<int:post_id>/addComment/', views.add_comment, name='addComment'),
    path('<int:comment_id>/addReply/', views.add_rely, name='addReply'),
    path('<int:comment_id>/repliesView/', views.repliesView, name='repliesView'),
    path('addPost/', views.add_post_view),
]
