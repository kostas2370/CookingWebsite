from django import forms
from .models import Recipe,comments
choices	=(("Desert","Desert"),("fastfood","fastfood"),("meat","meat"))
class recipe(forms.ModelForm):
	
	food_name=forms.CharField(max_length=50)
	
	

	class Meta:
		model=Recipe
		fields=["food_name","category","content","ingridients","image"]

class comment_form(forms.ModelForm):
	
	
	class Meta:
		model=comments
		fields=["comment"]
