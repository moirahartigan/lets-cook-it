from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe



class HomeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3
    


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


class RecipeDetail(View):
   
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "liked": liked,
            },
        )


class RecipeLike(View):

    def recipe(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
        

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['categories', 'title', 'slug', 'image_url', 'recipe_url', 'author', 'ingredients', 'method', 'prep_time', 'cook_time', 'servings']
    template_name = 'recipe_form.html'

    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
