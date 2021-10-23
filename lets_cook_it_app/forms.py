from django import forms
from .models import Comment, Categories


class RecipeCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('message',)

