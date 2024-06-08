from django import forms
from django.contrib.auth.forms import UserCreationForm

from store.models import Post


class CustomUserCreationForm(UserCreationForm):
    pass


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'content']
