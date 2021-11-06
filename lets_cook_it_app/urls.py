from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.RecipeCreateView.as_view(), name='create'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('search', views.SearchView, name='search_results'),
    path('profile/', views.ProfileRecipes.as_view(), name='profile'),
    path('<slug:slug>', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('edit/<slug:slug>', views.RecipeEdit.as_view(), name='recipe_edit'),
    path('delete/<slug:slug>', views.RecipeDelete.as_view(), name='recipe_delete'),
    path('', views.HomeList.as_view(), name='home'),
]
