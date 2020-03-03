from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class register_form(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField(max_value=99999999)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "phone", "password1", "password2"]


class Add_New_Comment(forms.Form):
    comment = forms.CharField()


class RawPostForm(forms.Form):
    post = forms.CharField()
    upload = forms.ImageField()


