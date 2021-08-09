from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length = 100)
	image = models.ImageField(upload_to='blog_images', default = 'default.jpg')
	content = RichTextUploadingField(blank=True, null=True)
	date_posted = models.DateTimeField()
	author = models.ForeignKey(User, on_delete= models.CASCADE)
	likes = models.ManyToManyField(User, related_name ='blogpost_likes')
	# comments = models.ForeignKey(Comment,on_delete=models.CASCADE)

	def get_likes(self):
		return self.likes.count()
	


class Comment(models.Model):
    Post = models.ForeignKey(BlogPost,related_name = "comments",on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    body = models.TextField(max_length=150)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s - %s' % (self.Post.title,self.author)