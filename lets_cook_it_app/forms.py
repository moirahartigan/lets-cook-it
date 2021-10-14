from django import forms
from .models import Recipe


class RecipeCreateForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ['categories', 'title', 'image', 'ingredients', 'method', 'prep_time', 'cook_time', 'servings' ]
