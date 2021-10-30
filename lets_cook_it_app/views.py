from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
# from django.db import models
from django.urls import reverse_lazy
# from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Categories
from .forms import RecipeCommentForm, CategoryForm, RecipeForm


class HomeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(
        status=1, approved=True).order_by('-created_on')
    template_name = 'index.html'


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(
        status=1, approved=True).order_by('-created_on')
    template_name = 'recipes.html'
    paginate_by = 6


class CategoryView(generic.ListView):
    model = Categories
    queryset = Recipe.objects.values('categories').distinct()
    template_name = 'categories.html'


# CRUD - Read functionality
class RecipeDetail(View):

    def get(self, request, slug):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                'comment_form': RecipeCommentForm()
            },
        )

    def post(self, request, slug):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by("-created_on")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = RecipeCommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = RecipeCommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                'comment_form': RecipeCommentForm()
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


# CRUD - Create functionality
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('profile')

# https://stackoverflow.com/questions/42481287/automatically-set-logged-in-user-as-the-author-in-django-using-createview-and-mo
    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.cleaned_data)
        return super().form_valid(form)


class AddCategoryView(LoginRequiredMixin, CreateView):
    model = Categories
    form_class = CategoryForm
    template_name = 'add_category.html'
    success_url = reverse_lazy('profile')


# CRUD - update functionality
class RecipeEdit(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_edit_form.html'

    def get_success_url(self):
        return reverse('recipe_detail', kwargs={'slug': self.object.slug})


# CRUD - Delete functionality
class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipe_delete_confirm.html'
    success_url = reverse_lazy('recipes')


# Search View
def SearchView(request):
    if request.method == "POST":
        searched = request.POST['searched']
        ingredients = Recipe.objects.filter(ingredients__contains=searched)

        return render(
            request,
            'search_results.html',
            {
                'searched': searched,
                'ingredients': ingredients
            }
        )
    else:
        return render(
            request,
            'search_results.html',
            {}
        )


# User Recipe View
class ProfileRecipes(View):

    def get(self, request):
        published_list = Recipe.objects.filter(status=1, author=request.user)
        draft_list = Recipe.objects.filter(status=0, author=request.user)

        return render(
            request,
            'profile.html',
            {
                'published_list': published_list,
                'draft_list': draft_list
            }
        )
