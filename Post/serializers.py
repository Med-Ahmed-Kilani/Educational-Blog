from rest_framework import serializers
from .models import Post, Comment

class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'url', 'post', 'createdAt', 'upload')

class Commentserializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'url', 'comment', 'createdAt', 'reply')