# from django.shortcuts import render
# from django.views.generic  import TemplateView, CreateView
# from .models import Categories, Recipe
# from .forms import RegistrationForm
# from django.urls import reverse_lazy

# class RecipeList(generic.ListView):
#     model = Recipe
#     queryset = Recipe.objects.filter(status=1)order_by('-created_on')
#     template_name = 'index.html'
#     )

# class HomeView(TemplateView):
#     template_name = 'lets_cook_it_app/home.html'

# class RegistrationView(CreateView):
#     from_class = RegistrationForm
#     success_url = reverse_lazy()
