from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image', 'status', 'password']
        labels = {
            'title': 'Post Title',
            'body': 'Text of your post',
            'image': 'Image:',
            'status': 'Status',
            'password': 'Access password',
        }


class PostAccess(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['password']
        labels = {
            'password': 'Access password'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        labels = {
            'name': 'Username',
            'body': 'Text of your comment',
        }



