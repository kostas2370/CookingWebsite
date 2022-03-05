from django.db import models

from django.contrib.auth.models import User


class Recipe (models.Model):
	food_name=models.CharField(max_length=50)
	category=models.TextField()
	content=models.TextField()
	maker=models.ForeignKey(User,on_delete=models.CASCADE)
	ingridients=models.TextField(default='0000000')
	