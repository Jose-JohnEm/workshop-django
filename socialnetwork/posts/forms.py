from django import forms
from .models import Post, Comments


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_content']
