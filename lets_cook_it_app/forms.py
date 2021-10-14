from django import forms
from .models import Recipe


class RecipeCreateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'method']
