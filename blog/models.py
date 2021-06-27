from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length = 100)
	image = models.ImageField(upload_to='blog_images', default = 'default.jpg')
	content = models.TextField()
	date_posted = models.DateTimeField()
	author = models.ForeignKey(User, on_delete= models.CASCADE)
