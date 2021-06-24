from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def post(request):
	context = {
		'blogs': BlogPost.objects.all()
	}
	return render(request, 'blog.html', context)

def index(request):
	return render(request, 'index.html')