from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe


class HomeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


class RecipeDetail(View):
    model = Recipe

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
            },
        )



class RegisterPage(generic.TemplateView):
    template_name = 'register.html'
    
