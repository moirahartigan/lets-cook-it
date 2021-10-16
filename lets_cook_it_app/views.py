from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import RecipeCreateForm


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
    model = Recipe

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

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        form = RecipeCreateForm(data=request.POST)

        # if form.is_valid():
        #     form.instance.email = request.user.email
        #     form.instance.name = request.user.username
        #     form.save()
        # else:
        #     form = RecipeCreateForm()


        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "liked": liked,
                "form": RecipeCreateForm()
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

        

class RecipeCreateView(generic.CreateView):
    model = Recipe

    def get(self, request, *args, **kwargs):
        context = {'form': RecipeCreateForm()}
        return render(request, 'recipes.html', context)

    def post(self, request, *args, **kwargs):
        context = {'form': RecipeCreateForm()}

        form = RecipeCreateForm(data=request.POST)

        # if form.is_valid():
        #     form.instance.email = request.user.email
        #     form.instance.name = request.user.username
        #     form.save()
        # else:
        #     form = RecipeCreateForm()
            
        return render(
            request,
            "recipes.html",
            {
                "uploaded": True,
                "form": RecipeCreateForm(),
            },
        )
        



    
