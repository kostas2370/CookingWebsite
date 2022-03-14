from django import forms
from .models import Recipe
choices	=(("Desert","Desert"),("fastfood","fastfood"),("meat","meat"))
class recipe(forms.ModelForm):
	category=forms.ChoiceField(choices=choices)
	food_name=forms.CharField(max_length=50)
	
	ingridients	=forms.CharField()	

	class Meta:
		model=Recipe
		fields=["food_name","category","content","ingridients","image"]