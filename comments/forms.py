from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    comment_id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Comment content',
        }
        help_texts = {
            'text': 'Enter your comment',
        }
