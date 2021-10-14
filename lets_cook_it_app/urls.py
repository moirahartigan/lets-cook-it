from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomeList.as_view(), name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipe/new/', views.RecipeCreate.as_view(), name='recipe_create'),
    # path('register/', views.RegisterPage.as_view(), name='register'),
    
]
