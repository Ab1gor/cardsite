from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Reply(models.Model):
	text = models.CharField(max_length=200)
	user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	def __str__(self):
		return str(self.id) + str(self.text)


class commentcount(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	card = models.ForeignKey('card.carddetails', on_delete=models.CASCADE)
	usercomment = models.CharField(max_length=200)
	reply = models.ManyToManyField(Reply, default=1)
	pub_date = timezone.now()
	def __str__(self):
		return str(self.card)



		