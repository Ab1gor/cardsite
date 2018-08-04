from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from likes.models import likecount
from comment.models import commentcount, Reply

# Create your models here.

class carddetails(models.Model):
	model_pic = models.ImageField(upload_to = 'image')
	user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
	title = models.CharField(max_length=200, unique=True)
	description = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published', default= timezone.now)
	private= models.BooleanField(default=False)
	
	#auto_increment_id = models.AutoField(primary_key=True, default=1, unique=True)
	def __str__(self):
		return self.title


