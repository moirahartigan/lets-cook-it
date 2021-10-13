from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Recipe

# class RecipeList(generic.listView):
#     model = Recipe
#     queryset = Recipe.objects.filter(ststus=1).order_by('-created_on')
#     template_name = 'index.html'

class RecipeView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    context_object_name = 'recipe'


class SingleView(DetailView):
    model = Recipe
    template_name = 'single.html'
    


class RecipeDetail(DetailView):
    model = Recipe
    
    def get(self, request, slug, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "recipe_detail.html"
        )
     
