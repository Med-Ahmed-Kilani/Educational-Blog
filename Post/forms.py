from django import forms
from .models import Post, Comment


class Add_New_Comment(forms.Form):
    comment = forms.CharField()


class RawPostForm(forms.Form):
    post = forms.CharField()
    upload = forms.ImageField()
