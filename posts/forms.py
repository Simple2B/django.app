from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'user']

        widgets = {
            'user': forms.HiddenInput()
        }
