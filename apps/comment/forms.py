from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        exclude = ['author', 'parent', 'post', 'top_level_comment_id', 'is_reply']
