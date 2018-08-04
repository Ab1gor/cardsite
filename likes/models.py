from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class likecount(models.Model):
    user = models.ManyToManyField(User, default= 1)
    card = models.OneToOneField('card.carddetails', on_delete=models.CASCADE ,  default = 1)
    def __str__(self):
    	return str(self.card) + '--' + str(self.user)
    # class Meta:
    # 	unique_together = (("user", "card"))
