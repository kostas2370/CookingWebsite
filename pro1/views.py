import requests
from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView,DetailView,CreateView


class RecipesListView(ListView):
	model= Recipe
	template_name="pro1/ask1.html"
	context_object_name ="syntages"
	ordering=['-id']

class RecipesDetailView(DetailView):
	
	model= Recipe
	template_name="pro1/syntagh.html"

class RecipeCreateView(CreateView):
	model= Recipe
	fields= ["food_name","category","content","ingridients"]
	template_name="pro1/syntagh_new.html"
	def form_valid(self,form):
		form.instance.maker = self.request.user
		return super().form_valid(form)


def ask2(request):
	return render(request,"pro1/ask2.html")

def contact(request):
	return render(request,"pro1/contact.html")
