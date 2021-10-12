from . import views
from django.urls import path

app_name = 'recipe'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('recipes/', views.RecipesView.as_view(), name='recipes'),
    path('<slug:slug>/', views.SingleView.as_view(), name='single'),
    
]
