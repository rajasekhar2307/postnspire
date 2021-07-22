from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from blog.models import BlogPost
from .serializers import blogPostSerializer
from rest_framework.response import Response

class blogPostView(APIView):

	def get(self, request):
		posts = BlogPost.objects.all()
		serializer = blogPostSerializer(posts, many = True)
		return Response(serializer.data)