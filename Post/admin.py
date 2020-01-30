from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'upload']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'reply', 'post']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

