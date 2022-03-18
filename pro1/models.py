from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
class category(models.Model):
		category=models.CharField(max_length=25)	
		def	__str__(self)	:
			return	self.category
class Recipe (models.Model):
	food_name=models.CharField(max_length=50)
	category=models.ForeignKey(category,on_delete=models.CASCADE)
	content=models.TextField()
	maker=models.ForeignKey(User,on_delete=models.CASCADE)
	ingridients=models.TextField(default='0000000')
	image=models.ImageField(default="default_food.jpg",upload_to="food",blank=True)		

	def get_absolute_url(self):
		return reverse("recipe-detail", kwargs={"pk":self.pk})

	def save(self):
		super().save()
		img= Image.open(self.image.path)
		if img.height >1280 or img.width >720:
			outputsize=(1280,720)
			img.thumbnail(outputsize)
			img.save(self.image.path)

class comments(models.Model):
	post=models.ForeignKey(Recipe,on_delete=models.CASCADE)
	commenter=models.ForeignKey(User,on_delete=models.CASCADE)
	comment=models.CharField(max_length=200)

