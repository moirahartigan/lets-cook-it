from . import views
from django.urls import path

app_name = 'recipe'

urlpatterns = [
    path('', views.RecipeView.as_view(), name='recipe'),
    path('recipes/', views.RecipeDetail.as_view(), name='recipes'),
    path('<slug:slug>/', views.SingleView.as_view(), name='single'),
    
]
