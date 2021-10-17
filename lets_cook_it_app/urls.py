from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('create/', views.RecipeCreateView.as_view(), name='create'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('<slug:slug>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('edit/<slug:slug>', views.RecipeEdit.as_view(), name='recipe_edit'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('', views.HomeList.as_view(), name='home'),
]  
