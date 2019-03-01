from django import forms
from .models import BlogPost
from markdownx.widgets import MarkdownxWidget


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'text', 'pic']
        labels = {
            'text': '',
            'pic': 'picture',
        }
        help_texts = {
            'pic': 'Upload the headline image of your post',
        }
        widgets = {
            'text': MarkdownxWidget(attrs={
                'placeholder': 'content',
                'style': 'height: 30rem;'
            })
        }

