from django.db import models
from django.contrib.auth.models import User


class userdetails(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
	about = models.CharField(max_length=200, default='Hey I am using CardsApp' )
	url = models.CharField(max_length=50, blank=True)
	company = models.CharField(max_length=50, blank=True)
	def __str__(self):
		return str(self.user)
