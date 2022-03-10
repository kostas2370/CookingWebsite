from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,UpdateUserForm,UpdateProfileForm
def register(request):
	if request.method=="POST":
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get("username")
			messages.success(request,f'Acount was made for {username}')
			return redirect("login")
	else:
		form=UserRegisterForm()
	
	return render(request, "users/register.html" , {'form':  form})

@login_required
def profile(request):

	return render(request,"users/profile.html")

@login_required
def settings(request):
	if (request.method=="POST"):
		uform=UpdateUserForm(request.POST,instance=request.user)
		pform=UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)	
		if uform.is_valid() and pform.is_valid():
			uform.save()
			pform.save()
			messages.success(request,f'Acount updated !')
			return redirect("profile")
	else:
		uform=UpdateUserForm(instance=request.user)
		pform=UpdateProfileForm(instance=request.user.profile)	
	context={
		"uform":uform,
		"pform":pform,
	}

	return render(request,"users/settings.html",context)