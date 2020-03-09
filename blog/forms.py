from django import forms

from .models import Post,Comment

class PostForm(forms.ModelForm):  #form for post

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm): #form for comment

    class Meta:
        model = Comment
        fields = ('author', 'text',)        