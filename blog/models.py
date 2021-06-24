from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length = 100)
	# image = models.ImageField(upload_to='images/')
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey(User, on_delete= models.CASCADE)