from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default_profile_pic.jpeg', upload_to='profile_pics')
	website = models.TextField(default='')
	name = models.TextField(max_length=20, default='')
	bio = models.TextField(max_length=80, default='')

	def __str__(self):
		return f'{self.user.username} Profile'