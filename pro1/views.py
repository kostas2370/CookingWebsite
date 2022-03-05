import requests
from django.shortcuts import render
from .models import Recipe
import random
def get_random():
   		return Recipe.objects.order_by("?").first()
def ask1(request):
	
	
	context={
		'syntages':[get_random()]
	}

	return render(request,"pro1/ask1.html",context)

def ask2(request):
	return render(request,"pro1/ask2.html")

def contact(request):
	return render(request,"pro1/contact.html")
