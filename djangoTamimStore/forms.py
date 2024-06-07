from django import forms
from django.contrib.auth.forms import UserCreationForm

from store.models import Post


class CustomUserCreationForm(UserCreationForm):
    pass


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']