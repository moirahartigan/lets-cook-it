from django import forms
from .models import Comment


class RecipeCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('message',)
