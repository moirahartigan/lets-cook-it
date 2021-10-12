from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Recipe


class IndexView(ListView):
    model = Recipe
    template_name = 'index.html'
    context_object_name = 'index'


class SingleView(DetailView):
    model = Recipe
    template_name = 'single.html'
    context_object_name = 'recipe'


class RecipesView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    context_object_name = 'recipe_list'
