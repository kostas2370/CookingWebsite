import requests
from django.shortcuts import render

url="https://api.chucknorris.io/jokes/random"



cringe_memes=[]
for i in range(5):
    response = requests.get(url)
    x= response.json()
    cringe_memes.append(x)




def ask1(request):
	context={
		'anekdota':cringe_memes

	}
	return render(request,"pro1/ask1.html",context)

def ask2(request):
	return render(request,"pro1/ask2.html")
