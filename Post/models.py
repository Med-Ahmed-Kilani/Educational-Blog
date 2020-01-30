from django.db import models


class Post(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    post = models.CharField(max_length=500)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    upload = models.ImageField(upload_to='uploads')
    likes = models.IntegerField(blank=True, default=0)
    dislikes = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return f"{self.post},{self.createdAt}"


class Comment(models.Model):

    id = models.AutoField(auto_created=True, primary_key=True)
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    comment = models.TextField(max_length=200)
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, related_name='replies')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='cmnts', null=True)
    likes = models.IntegerField(blank=True, default=0)
    dislikes = models.IntegerField(blank=True, default=0)


    def __str__(self):
        return f"{self.id},{self.comment},{self.createdAt}"



