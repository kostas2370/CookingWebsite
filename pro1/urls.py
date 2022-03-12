from django.urls import path
from . import views
from .views import RecipesListView,RecipesDetailView,RecipeCreateView
urlpatterns = [
    path('', RecipesListView.as_view(),name="home"),
    path('recipe/<int:pk>/', RecipesDetailView.as_view(),name="recipe-detail"),
    path('recipe/new/', RecipeCreateView.as_view(),name="recipe-new"),
    path('about/', views.ask2,name="about"),
    path('contact/', views.contact,name="contact")

]