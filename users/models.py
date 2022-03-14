from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class profile (models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default="default.jpg",upload_to="profile_pics")
	description=models.TextField(default="")
	def __str__(self):
		return f'{self.user.username} profile'

	def save(self,*args, **kwargs):
		super().save()
		img= Image.open(self.image.path)	
		if img.height >300 or img.width >300:
			outputsize=(300,300)
			img.thumbnail(outputsize)
			img.save(self.image.path)	
