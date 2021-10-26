from django import forms
from .models import Recipe, Comment, Categories
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextField


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['title', 'categories', 'image_url', 'recipe_url', 'author', 'ingredients', 'method', 'prep_time', 'cook_time', 'servings']
        widgets = {
            'method': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }


class RecipeCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('message',)

