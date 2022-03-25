import requests
from django.shortcuts import render,redirect
from .models import Recipe,comments
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .forms import recipe,comment_form
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
class RecipesListView(ListView):
    model= Recipe
    template_name="pro1/ask1.html"
    context_object_name ="syntages"
    ordering=['-id']
    paginate_by=3    
class RecipesDetailView(DetailView):
    
    model= Recipe
    template_name="pro1/syntagh.html"
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = comments.objects.filter(
            post=self.get_object())
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['form'] = comment_form(instance=self.request.user)
        return data

    def post(self, request, *args, **kwargs):
        new_comment = comments(comment=request.POST.get('comment'),
                                  commenter=self.request.user,
                                  post=self.get_object())
        new_comment.save()
     	
        return HttpResponseRedirect(self.request.path_info)     

class RecipeCreateView(CreateView):
    model= Recipe
    template_name="pro1/syntagh_new.html"
    form_class = recipe
    def form_valid(self,form):
        form.instance.maker = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(UpdateView,LoginRequiredMixin,UserPassesTestMixin):
    model= Recipe
    template_name="pro1/syntagh_update.html"
    fields=["food_name","category","content","ingridients","image"]
    
    def form_valid(self, form):
        form.instance.maker = self.request.user
        return super().form_valid(form)

    
  


        



def ask2(request):
    return render(request,"pro1/ask2.html")

def contact(request):
    return render(request,"pro1/contact.html")

