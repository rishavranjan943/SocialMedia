from .models import *
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image','caption')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)