from rest_framework import serializers
from blog.models import BlogPost

class blogPostSerializer(serializers.ModelSerializer):

	class Meta:
		model = BlogPost
		fields = '__all__'