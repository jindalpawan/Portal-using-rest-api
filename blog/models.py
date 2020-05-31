from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

class Post(models.Model):
	author= models.ForeignKey(User, on_delete=models.CASCADE)
	title= models.TextField()
	content=models.TextField()
	likes=models.ManyToManyField(User, related_name='likes')
	create_date=models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return self.title

	def datecreated(self):
		return self.create_date.strftime('%d %b, %Y')

	def Content(self):
		return self.content[:200]+"..."

	def Contents(self):
		return self.content[:100]+"..."

	def total_likes(self):
		return self.likes.count()
