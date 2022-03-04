import requests
from django.shortcuts import render



def ask1(request):
	url="http://www.themealdb.com/api/json/v1/1/random.php"
	syntages=[]
	for i in range(5):
		response = requests.get(url)
		x=response.json()["meals"][0]
		syntages.append(x)
		
	
	context={
		'syntages':syntages
	}

	return render(request,"pro1/ask1.html",context)

def ask2(request):
	return render(request,"pro1/ask2.html")
