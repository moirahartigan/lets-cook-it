from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import RecipeCreateForm


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


class RecipeCreateView(generic.CreateView):
    model = Recipe

    def get(self, request, *args, **kwargs):
        context = {'form': RecipeCreateForm()}
        return render(request, 'recipes/recipe_form.html', context)

    def post(self, request, *args, **kwargs):
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.save()
            return HttpResponseRedirect(reverse('recipes:detail', args=[slug]))
        return render(request, 'recipes/recipe_form.html', {'form': form})


class RegisterPage(generic.TemplateView):
    template_name = 'register.html'
    
