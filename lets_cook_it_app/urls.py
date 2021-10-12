from . import views
from django.urls import path

app_name = 'lets_cook_it_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
